from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id
from utils.enums.status_bencana import StatusBencana
from utils.enum_parser import parse_enum

from models.bencana import Bencana
from repositories.base_repository import BaseRepository


class BencanaService:
    """
    Service untuk alur bisnis Bencana.

    Tanggung jawab:
    - Generate id_bencana (via helper)
    - Konversi status string -> StatusBencana (Enum)
    - Membuat & memvalidasi objek Bencana
    - Memanggil repository (CRUD) melalui abstraksi (DIP)
    """

    def __init__(self, repo: BaseRepository):
        """
        Inisialisasi BencanaService.

        Args:
            repo (BaseRepository): Repository Bencana (di-inject).
        """
        self._repo = repo
        self._logger = get_logger(__name__)

    # ===== CREATE =====
    def buat_bencana(
        self,
        jenis: str,
        lokasi: str,
        tanggal_mulai: date,
        status: str,
    ) -> str:
        """
        Membuat bencana baru dan menyimpannya ke repository.

        Args:
            jenis (str): Jenis bencana.
            lokasi (str): Lokasi kejadian.
            tanggal_mulai (date): Tanggal mulai bencana.
            status (str): Status bencana ("aktif", "siaga", "selesai").

        Returns:
            str: id_bencana yang berhasil dibuat.

        Raises:
            ValueError: Jika parsing enum atau validasi model gagal.
            RuntimeError: Jika repository menolak penyimpanan.
        """
        id_bencana = generate_id()
        status_enum: StatusBencana = parse_enum(StatusBencana, status)

        self._logger.info(
            f"Membuat bencana baru id_bencana={id_bencana}, status={status_enum.value} ({datetime.now()})"
        )

        # Setter dipanggil otomatis di constructor model
        bencana = Bencana(
            id_bencana=id_bencana,
            jenis=jenis,
            lokasi=lokasi,
            tanggal_mulai=tanggal_mulai,
            status=status_enum,
        )

        if not self._repo.tambah(bencana):
            self._logger.error(
                f"Gagal menyimpan bencana id_bencana={id_bencana} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan bencana (ID duplikat).")

        return id_bencana

    # ===== READ =====
    def ambil_bencana(self, id_bencana: str) -> Bencana | None:
        """
        Mengambil bencana berdasarkan ID.
        """
        self._logger.info(
            f"Mengambil bencana id_bencana={id_bencana} ({datetime.now()})"
        )
        return self._repo.ambil_berdasarkan_id(id_bencana)

    def ambil_semua_bencana(self) -> list[Bencana]:
        """
        Mengambil semua data bencana.
        """
        self._logger.info(f"Mengambil semua bencana ({datetime.now()})")
        return self._repo.ambil_semua()

    # ===== UPDATE =====
    def perbarui_bencana(
        self,
        id_bencana: str,
        jenis: str,
        lokasi: str,
        tanggal_mulai: date,
        status: str,
    ) -> bool:
        """
        Memperbarui data bencana berdasarkan ID.
        """
        existing = self._repo.ambil_berdasarkan_id(id_bencana)
        if existing is None:
            self._logger.warning(
                f"Gagal perbarui: bencana id_bencana={id_bencana} tidak ditemukan ({datetime.now()})"
            )
            return False

        status_enum: StatusBencana = parse_enum(StatusBencana, status)

        # Buat object baru agar validasi model tetap dijalankan
        bencana_baru = Bencana(
            id_bencana=id_bencana,
            jenis=jenis,
            lokasi=lokasi,
            tanggal_mulai=tanggal_mulai,
            status=status_enum,
        )

        sukses = self._repo.perbarui(id_bencana, bencana_baru)
        if sukses:
            self._logger.info(
                f"Bencana id_bencana={id_bencana} berhasil diperbarui ({datetime.now()})"
            )

        return sukses

    # ===== DELETE =====
    def hapus_bencana(self, id_bencana: str) -> bool:
        """
        Menghapus bencana berdasarkan ID.
        """
        self._logger.info(
            f"Menghapus bencana id_bencana={id_bencana} ({datetime.now()})"
        )
        sukses = self._repo.hapus(id_bencana)

        if sukses:
            self._logger.info(
                f"Bencana id_bencana={id_bencana} berhasil dihapus ({datetime.now()})"
            )
        else:
            self._logger.warning(
                f"Gagal hapus: bencana id_bencana={id_bencana} tidak ditemukan ({datetime.now()})"
            )

        return sukses

    # ===== PARTIAL UPDATE (OPSIONAL) =====
    def ubah_status_bencana(self, id_bencana: str, status: str) -> bool:
        """
        Mengubah status bencana saja.
        """
        bencana = self._repo.ambil_berdasarkan_id(id_bencana)
        if bencana is None:
            self._logger.warning(
                f"Gagal ubah status: bencana id_bencana={id_bencana} tidak ditemukan ({datetime.now()})"
            )
            return False

        status_enum: StatusBencana = parse_enum(StatusBencana, status)

        # Setter model dipanggil langsung
        bencana.set_status(status_enum)

        sukses = self._repo.perbarui(id_bencana, bencana)
        if sukses:
            self._logger.info(
                f"Status bencana id_bencana={id_bencana} diubah menjadi {status_enum.value} ({datetime.now()})"
            )

        return sukses
