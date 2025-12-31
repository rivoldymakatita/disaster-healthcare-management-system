from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id

from models.resep_obat import ResepObat
from models.resep_item import ResepItem
from models.obat import Obat
from models.pemeriksaan import Pemeriksaan

from repositories.base_repository import BaseRepository


class ResepObatService:
    """
    Service untuk alur bisnis ResepObat.

    Tanggung jawab:
    - Generate id_resep
    - Validasi FK: Pemeriksaan harus ada
    - Validasi FK: Obat harus ada
    - Validasi stok: stok tidak boleh negatif
    - Kurangi stok obat sesuai qty
    - Simpan resep ke repository
    """

    def __init__(
        self,
        resep_repo: BaseRepository,
        pemeriksaan_repo: BaseRepository,
        obat_repo: BaseRepository,
    ):
        self._resep_repo = resep_repo
        self._pemeriksaan_repo = pemeriksaan_repo
        self._obat_repo = obat_repo
        self._logger = get_logger(__name__)

    def buat_resep(
        self,
        id_pemeriksaan: str,
        items_input: list[dict],
        tanggal_resep: date | None = None,
    ) -> str:
        """
        Membuat resep berdasarkan pemeriksaan + daftar item.

        items_input format (contoh):
        [
          {"id_obat": "...", "qty": 2, "aturan_pakai": "2x1", "dosis": 1},
          {"id_obat": "...", "qty": 1, "aturan_pakai": "1x1", "dosis": 1},
        ]
        """
        now = datetime.now()
        self._logger.info(f"Membuat resep obat baru ({now})")

        # ===== FK: pemeriksaan harus ada =====
        pemeriksaan: Pemeriksaan | None = self._pemeriksaan_repo.ambil_berdasarkan_id(id_pemeriksaan)
        if pemeriksaan is None:
            raise ValueError("Pemeriksaan tidak ditemukan")

        if not isinstance(items_input, list) or len(items_input) == 0:
            raise ValueError("Items resep tidak boleh kosong")

        if tanggal_resep is None:
            tanggal_resep = date.today()

        # ===== Siapkan item + validasi stok dulu (tanpa mengubah stok) =====
        # Gabungkan item dengan id_obat sama (opsional tapi lebih aman)
        merged_items: dict[str, dict] = {}
        for item in items_input:
            if not isinstance(item, dict):
                raise ValueError("Format item resep harus dict")

            id_obat = item.get("id_obat")
            qty = item.get("qty")
            aturan_pakai = item.get("aturan_pakai")
            dosis = item.get("dosis")

            if not isinstance(id_obat, str) or not id_obat.strip():
                raise ValueError("id_obat tidak valid")

            if not isinstance(qty, int) or qty <= 0:
                raise ValueError("qty harus integer positif")

            if not isinstance(aturan_pakai, str) or not aturan_pakai.strip():
                raise ValueError("aturan_pakai tidak boleh kosong")

            if not isinstance(dosis, int) or dosis <= 0:
                raise ValueError("dosis harus integer positif")

            if id_obat not in merged_items:
                merged_items[id_obat] = {
                    "id_obat": id_obat,
                    "qty": qty,
                    "aturan_pakai": aturan_pakai,
                    "dosis": dosis,
                }
            else:
                # gabung qty
                merged_items[id_obat]["qty"] += qty
                # aturan_pakai & dosis tetap ambil yang pertama (atau kamu bisa pakai yang terakhir)

        resep_items: list[ResepItem] = []
        stok_awal: dict[str, int] = {}  # id_obat -> stok sebelum transaksi

        for id_obat, item in merged_items.items():
            obat: Obat | None = self._obat_repo.ambil_berdasarkan_id(id_obat)
            if obat is None:
                raise ValueError(f"Obat tidak ditemukan (id_obat={id_obat})")

            # simpan stok awal untuk rollback
            stok_awal[id_obat] = obat.get_stok()

            if obat.get_stok() < item["qty"]:
                raise ValueError(f"Stok obat '{obat.get_nama()}' tidak cukup")

            resep_items.append(
                ResepItem(
                    obat=obat,
                    qty=item["qty"],
                    aturan_pakai=item["aturan_pakai"],
                    dosis=item["dosis"],
                )
            )

        # ===== Jika semua valid, baru kurangi stok (transaksi) =====
        changed_obats: list[Obat] = []

        try:
            for resep_item in resep_items:
                obat = resep_item.get_obat()
                id_obat = obat.get_id_obat()

                stok_baru = obat.get_stok() - resep_item.get_qty()
                obat.set_stok(stok_baru)

                if not self._obat_repo.perbarui(id_obat, obat):
                    raise RuntimeError(f"Gagal update stok obat (id_obat={id_obat})")

                changed_obats.append(obat)
                self._logger.info(
                    f"Stok obat id_obat={id_obat} dikurangi qty={resep_item.get_qty()} ({now})"
                )

            # ===== Buat & simpan resep =====
            id_resep = generate_id()
            resep = ResepObat(
                id_resep=id_resep,
                pemeriksaan=pemeriksaan,
                items=resep_items,
                tanggal_resep=tanggal_resep,
            )

            if not self._resep_repo.tambah(resep):
                raise RuntimeError("Gagal menyimpan resep (ID duplikat)")

            self._logger.info(f"Resep id_resep={id_resep} berhasil dibuat ({now})")
            return id_resep

        except Exception as e:
            # ===== ROLLBACK stok =====
            self._logger.error(f"Transaksi resep gagal, rollback stok... ({now})")

            for obat in changed_obats:
                id_obat = obat.get_id_obat()
                if id_obat in stok_awal:
                    try:
                        obat.set_stok(stok_awal[id_obat])
                        if not self._obat_repo.perbarui(id_obat, obat):
                            self._logger.error(f"Rollback gagal update repo untuk id_obat={id_obat} ({now})")
                    except Exception:
                        self._logger.error(f"Rollback gagal untuk id_obat={id_obat} ({now})")

            raise e

    def ambil_resep(self, id_resep: str) -> ResepObat | None:
        self._logger.info(f"Mengambil resep id_resep={id_resep} ({datetime.now()})")
        return self._resep_repo.ambil_berdasarkan_id(id_resep)

    def ambil_semua_resep(self) -> list[ResepObat]:
        self._logger.info(f"Mengambil semua resep ({datetime.now()})")
        return self._resep_repo.ambil_semua()

    def hapus_resep(self, id_resep: str) -> bool:
        self._logger.info(f"Menghapus resep id_resep={id_resep} ({datetime.now()})")
        return self._resep_repo.hapus(id_resep)
