from datetime import datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id
from utils.enums.status_posko import StatusPosko
from utils.enums.status_bencana import StatusBencana
from utils.enum_parser import parse_enum

from models.posko import Posko
from models.bencana import Bencana
from repositories.base_repository import BaseRepository


class PoskoService:
    """
    Service untuk alur bisnis Posko.

    Tanggung jawab:
    - Generate id_posko
    - Validasi FK ke Bencana
    - Konversi status_posko string -> StatusPosko (Enum)
    - Membuat & memvalidasi objek Posko
    - Memanggil repository Posko melalui abstraksi (DIP)
    """

    def __init__(
        self,
        posko_repo: BaseRepository,
        bencana_repo: BaseRepository,
    ):
        """
        Inisialisasi PoskoService.

        Args:
            posko_repo (BaseRepository): Repository Posko.
            bencana_repo (BaseRepository): Repository Bencana.
        """
        self._posko_repo = posko_repo
        self._bencana_repo = bencana_repo
        self._logger = get_logger(__name__)

    # ===== CREATE =====
    def buat_posko(
        self,
        bencana_id: str,
        nama_posko: str,
        alamat_posko: str,
        kapasitas_posko: int,
        status_posko: str,
    ) -> str:
        """
        Membuat posko baru dan menyimpannya ke repository.

        Args:
            bencana_id (str): ID bencana terkait.
            nama_posko (str): Nama posko.
            alamat_posko (str): Alamat posko.
            kapasitas_posko (int): Kapasitas posko.
            status_posko (str): Status posko ("aktif", "siaga", "tutup", dll).

        Returns:
            str: id_posko yang berhasil dibuat.

        Raises:
            ValueError: Jika bencana tidak valid atau status enum tidak valid.
            RuntimeError: Jika repository menolak penyimpanan.
        """
        self._logger.info(
            f"Membuat posko untuk bencana_id={bencana_id} ({datetime.now()})"
        )

        # ===== Validasi FK: Bencana harus ada =====
        bencana: Bencana | None = self._bencana_repo.ambil_berdasarkan_id(bencana_id)
        if bencana is None:
            raise ValueError("Bencana tidak ditemukan")

        # ===== Contoh aturan bisnis =====
        if bencana.get_status() == StatusBencana.SELESAI:
            raise ValueError("Tidak dapat membuat posko untuk bencana yang sudah selesai")

        id_posko = generate_id()
        status_enum: StatusPosko = parse_enum(StatusPosko, status_posko)

        posko = Posko(
            id_posko=id_posko,
            bencana=bencana,
            nama_posko=nama_posko,
            alamat_posko=alamat_posko,
            kapasitas_posko=kapasitas_posko,
            status_posko=status_enum,
        )

        if not self._posko_repo.tambah(posko):
            self._logger.error(
                f"Gagal menyimpan posko id_posko={id_posko} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan posko (ID duplikat).")

        self._logger.info(
            f"Posko id_posko={id_posko} berhasil dibuat ({datetime.now()})"
        )
        return id_posko

    # ===== READ =====
    def ambil_posko(self, id_posko: str) -> Posko | None:
        """
        Mengambil posko berdasarkan ID.
        """
        self._logger.info(
            f"Mengambil posko id_posko={id_posko} ({datetime.now()})"
        )
        return self._posko_repo.ambil_berdasarkan_id(id_posko)

    def ambil_semua_posko(self) -> list[Posko]:
        """
        Mengambil semua data posko.
        """
        self._logger.info(f"Mengambil semua posko ({datetime.now()})")
        return self._posko_repo.ambil_semua()

    # ===== UPDATE =====
    def perbarui_posko(
        self,
        id_posko: str,
        bencana_id: str,
        nama_posko: str,
        alamat_posko: str,
        kapasitas_posko: int,
        status_posko: str,
    ) -> bool:
        """
        Memperbarui data posko berdasarkan ID.
        """
        existing = self._posko_repo.ambil_berdasarkan_id(id_posko)
        if existing is None:
            self._logger.warning(
                f"Gagal perbarui: posko id_posko={id_posko} tidak ditemukan ({datetime.now()})"
            )
            return False

        bencana = self._bencana_repo.ambil_berdasarkan_id(bencana_id)
        if bencana is None:
            raise ValueError("Bencana tidak ditemukan")

        status_enum: StatusPosko = parse_enum(StatusPosko, status_posko)

        posko_baru = Posko(
            id_posko=id_posko,
            bencana=bencana,
            nama_posko=nama_posko,
            alamat_posko=alamat_posko,
            kapasitas_posko=kapasitas_posko,
            status_posko=status_enum,
        )

        sukses = self._posko_repo.perbarui(id_posko, posko_baru)
        if sukses:
            self._logger.info(
                f"Posko id_posko={id_posko} berhasil diperbarui ({datetime.now()})"
            )

        return sukses

    # ===== DELETE =====
    def hapus_posko(self, id_posko: str) -> bool:
        """
        Menghapus posko berdasarkan ID.
        """
        self._logger.info(
            f"Menghapus posko id_posko={id_posko} ({datetime.now()})"
        )
        sukses = self._posko_repo.hapus(id_posko)

        if sukses:
            self._logger.info(
                f"Posko id_posko={id_posko} berhasil dihapus ({datetime.now()})"
            )
        else:
            self._logger.warning(
                f"Gagal hapus: posko id_posko={id_posko} tidak ditemukan ({datetime.now()})"
            )

        return sukses

    # ===== PARTIAL UPDATE (OPSIONAL) =====
    def ubah_status_posko(self, id_posko: str, status_posko: str) -> bool:
        """
        Mengubah status posko saja.
        """
        posko = self._posko_repo.ambil_berdasarkan_id(id_posko)
        if posko is None:
            self._logger.warning(
                f"Gagal ubah status: posko id_posko={id_posko} tidak ditemukan ({datetime.now()})"
            )
            return False

        status_enum: StatusPosko = parse_enum(StatusPosko, status_posko)

        posko.set_status_posko(status_enum)

        sukses = self._posko_repo.perbarui(id_posko, posko)
        if sukses:
            self._logger.info(
                f"Status posko id_posko={id_posko} diubah menjadi {status_enum.value} ({datetime.now()})"
            )

        return sukses