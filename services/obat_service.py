from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id

from models.obat import Obat
from repositories.base_repository import BaseRepository


class ObatService:
    def __init__(self, obat_repo: BaseRepository):
        self._obat_repo = obat_repo
        self._logger = get_logger(__name__)

    # ===== CREATE =====
    def buat_obat(
        self,
        nama: str,
        stok: int,
        satuan: str,
        tanggal_kadaluarsa: date,
    ) -> str:
        now = datetime.now()
        self._logger.info(f"Membuat obat baru ({now})")

        if isinstance(tanggal_kadaluarsa, date) and tanggal_kadaluarsa < date.today():
            raise ValueError("Tanggal kadaluarsa tidak boleh di masa lalu")

        id_obat = generate_id()
        # Perhatikan: parameter disesuaikan dengan models/obat.py
        obat = Obat(
            id_obat=id_obat,
            nama_obat=nama,
            stock_obat=stok,
            satuan_obat=satuan,
            tanggal_kadaluarsa_obat=tanggal_kadaluarsa,
        )

        if not self._obat_repo.tambah(obat):
            self._logger.error(f"Gagal simpan obat id_obat={id_obat} ({datetime.now()})")
            raise RuntimeError("Gagal menyimpan obat (ID duplikat)")

        self._logger.info(f"Obat id_obat={id_obat} berhasil dibuat ({datetime.now()})")
        return id_obat

    # ===== READ =====
    def ambil_obat(self, id_obat: str) -> Obat | None:
        self._logger.info(f"Mengambil obat id_obat={id_obat} ({datetime.now()})")
        return self._obat_repo.ambil_berdasarkan_id(id_obat)

    def ambil_semua_obat(self) -> list[Obat]:
        self._logger.info(f"Mengambil semua obat ({datetime.now()})")
        return self._obat_repo.ambil_semua()

    # ===== UPDATE =====
    def perbarui_obat(
        self,
        id_obat: str,
        nama: str,
        stok: int,
        satuan: str,
        tanggal_kadaluarsa: date,
    ) -> bool:
        now = datetime.now()
        existing = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if existing is None:
            self._logger.warning(f"Gagal update: obat id_obat={id_obat} tidak ditemukan ({now})")
            return False

        if tanggal_kadaluarsa < date.today():
            raise ValueError("Tanggal kadaluarsa tidak boleh di masa lalu")

        obat_baru = Obat(
            id_obat=id_obat,
            nama_obat=nama,
            stock_obat=stok,
            satuan_obat=satuan,
            tanggal_kadaluarsa_obat=tanggal_kadaluarsa,
        )

        sukses = self._obat_repo.perbarui(id_obat, obat_baru)
        if sukses:
            self._logger.info(f"Obat id_obat={id_obat} berhasil diperbarui ({datetime.now()})")
        return sukses

    # ===== DELETE =====
    def hapus_obat(self, id_obat: str) -> bool:
        self._logger.info(f"Menghapus obat id_obat={id_obat} ({datetime.now()})")
        sukses = self._obat_repo.hapus(id_obat)

        if sukses:
            self._logger.info(f"Obat id_obat={id_obat} berhasil dihapus ({datetime.now()})")
        else:
            self._logger.warning(f"Gagal hapus: obat id_obat={id_obat} tidak ditemukan ({datetime.now()})")

        return sukses

    # ===== STOCK OPS =====
    def tambah_stok(self, id_obat: str, qty: int) -> bool:
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Qty harus integer positif")

        now = datetime.now()
        obat = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if obat is None:
            self._logger.warning(f"Gagal tambah stok: obat id_obat={id_obat} tidak ditemukan ({now})")
            return False

        # Perbaikan nama method getter/setter
        stok_baru = obat.get_stock_obat() + qty
        obat.set_stock_obat(stok_baru)

        sukses = self._obat_repo.perbarui(id_obat, obat)
        if sukses:
            self._logger.info(f"Stok obat id_obat={id_obat} ditambah qty={qty} ({datetime.now()})")
        return sukses

    def kurangi_stok(self, id_obat: str, qty: int) -> bool:
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Qty harus integer positif")

        now = datetime.now()
        obat = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if obat is None:
            self._logger.warning(f"Gagal kurangi stok: obat id_obat={id_obat} tidak ditemukan ({now})")
            return False

        # Perbaikan nama method getter
        stok_saat_ini = obat.get_stock_obat()
        if stok_saat_ini < qty:
            self._logger.warning(
                f"Gagal kurangi stok: stok tidak cukup id_obat={id_obat} stok={stok_saat_ini} qty={qty} ({now})"
            )
            return False

        # Perbaikan nama method setter
        obat.set_stock_obat(stok_saat_ini - qty)

        sukses = self._obat_repo.perbarui(id_obat, obat)
        if sukses:
            self._logger.info(f"Stok obat id_obat={id_obat} dikurangi qty={qty} ({datetime.now()})")
        return sukses

    # ===== HELPERS =====
    def cek_kadaluarsa(self, id_obat: str) -> bool:
        obat = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if obat is None:
            return False
        # Perbaikan nama method getter
        return obat.get_tanggal_kadaluarsa_obat() < date.today()