from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id

from models.obat import Obat
from repositories.base_repository import BaseRepository


class ObatService:
    """
    Service untuk alur bisnis Obat.

    Tanggung jawab:
    - Generate id_obat
    - Membuat & memvalidasi object Obat
    - CRUD Obat
    - Operasi stok (tambah/kurangi) dengan aturan stok tidak boleh negatif
    """

    def __init__(self, obat_repo: BaseRepository):
        """
        Inisialisasi ObatService.

        Args:
            obat_repo (BaseRepository): Repository Obat (DIP).
        """
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
        """
        Membuat data obat baru.

        Args:
            nama (str): Nama obat.
            stok (int): Stok awal.
            satuan (str): Satuan obat (Tablet, Botol, dll).
            tanggal_kadaluarsa (date): Tanggal kadaluarsa.

        Returns:
            str: id_obat yang dibuat.

        Raises:
            ValueError: Jika tanggal kadaluarsa sudah lewat (opsional).
            RuntimeError: Jika gagal simpan.
        """
        now = datetime.now()
        self._logger.info(f"Membuat obat baru ({now})")

        # validasi bisnis (opsional tapi bagus)
        if isinstance(tanggal_kadaluarsa, date) and tanggal_kadaluarsa < date.today():
            raise ValueError("Tanggal kadaluarsa tidak boleh di masa lalu")

        id_obat = generate_id()
        obat = Obat(
            id_obat=id_obat,
            nama=nama,
            stok=stok,
            satuan=satuan,
            tanggal_kadaluarsa=tanggal_kadaluarsa,
        )

        if not self._obat_repo.tambah(obat):
            self._logger.error(f"Gagal simpan obat id_obat={id_obat} ({datetime.now()})")
            raise RuntimeError("Gagal menyimpan obat (ID duplikat)")

        self._logger.info(f"Obat id_obat={id_obat} berhasil dibuat ({datetime.now()})")
        return id_obat

    # ===== READ =====
    def ambil_obat(self, id_obat: str) -> Obat | None:
        """Mengambil obat berdasarkan id_obat."""
        self._logger.info(f"Mengambil obat id_obat={id_obat} ({datetime.now()})")
        return self._obat_repo.ambil_berdasarkan_id(id_obat)

    def ambil_semua_obat(self) -> list[Obat]:
        """Mengambil semua obat."""
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
        """
        Memperbarui data obat.

        Returns:
            bool: True jika sukses, False jika id tidak ditemukan.
        """
        now = datetime.now()
        existing = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if existing is None:
            self._logger.warning(f"Gagal update: obat id_obat={id_obat} tidak ditemukan ({now})")
            return False

        if tanggal_kadaluarsa < date.today():
            raise ValueError("Tanggal kadaluarsa tidak boleh di masa lalu")

        obat_baru = Obat(
            id_obat=id_obat,
            nama=nama,
            stok=stok,
            satuan=satuan,
            tanggal_kadaluarsa=tanggal_kadaluarsa,
        )

        sukses = self._obat_repo.perbarui(id_obat, obat_baru)
        if sukses:
            self._logger.info(f"Obat id_obat={id_obat} berhasil diperbarui ({datetime.now()})")
        return sukses

    # ===== DELETE =====
    def hapus_obat(self, id_obat: str) -> bool:
        """Menghapus obat berdasarkan id_obat."""
        self._logger.info(f"Menghapus obat id_obat={id_obat} ({datetime.now()})")
        sukses = self._obat_repo.hapus(id_obat)

        if sukses:
            self._logger.info(f"Obat id_obat={id_obat} berhasil dihapus ({datetime.now()})")
        else:
            self._logger.warning(f"Gagal hapus: obat id_obat={id_obat} tidak ditemukan ({datetime.now()})")

        return sukses

    # ===== STOCK OPS =====
    def tambah_stok(self, id_obat: str, qty: int) -> bool:
        """
        Menambah stok obat.

        Args:
            id_obat (str): ID obat.
            qty (int): Jumlah tambahan stok (positif).

        Returns:
            bool: True jika sukses.
        """
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Qty harus integer positif")

        now = datetime.now()
        obat = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if obat is None:
            self._logger.warning(f"Gagal tambah stok: obat id_obat={id_obat} tidak ditemukan ({now})")
            return False

        stok_baru = obat.get_stok() + qty
        obat.set_stok(stok_baru)

        sukses = self._obat_repo.perbarui(id_obat, obat)
        if sukses:
            self._logger.info(f"Stok obat id_obat={id_obat} ditambah qty={qty} ({datetime.now()})")
        return sukses

    def kurangi_stok(self, id_obat: str, qty: int) -> bool:
        """
        Mengurangi stok obat.

        Aturan:
        - qty harus positif
        - stok tidak boleh negatif

        Returns:
            bool: True jika sukses.
        """
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Qty harus integer positif")

        now = datetime.now()
        obat = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if obat is None:
            self._logger.warning(f"Gagal kurangi stok: obat id_obat={id_obat} tidak ditemukan ({now})")
            return False

        stok_saat_ini = obat.get_stok()
        if stok_saat_ini < qty:
            self._logger.warning(
                f"Gagal kurangi stok: stok tidak cukup id_obat={id_obat} stok={stok_saat_ini} qty={qty} ({now})"
            )
            return False

        obat.set_stok(stok_saat_ini - qty)

        sukses = self._obat_repo.perbarui(id_obat, obat)
        if sukses:
            self._logger.info(f"Stok obat id_obat={id_obat} dikurangi qty={qty} ({datetime.now()})")
        return sukses

    # ===== HELPERS =====
    def cek_kadaluarsa(self, id_obat: str) -> bool:
        """
        Mengecek apakah obat sudah kadaluarsa.

        Returns:
            bool: True jika kadaluarsa, False jika tidak / tidak ditemukan.
        """
        obat = self._obat_repo.ambil_berdasarkan_id(id_obat)
        if obat is None:
            return False
        return obat.get_tanggal_kadaluarsa() < date.today()
