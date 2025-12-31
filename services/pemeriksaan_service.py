from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id
from utils.enums.status_triase import StatusTriase
from utils.enum_parser import parse_enum

from models.pemeriksaan import Pemeriksaan
from models.korban import Korban
from models.tenaga_medis import TenagaMedis

from repositories.base_repository import BaseRepository


class PemeriksaanService:
    """
    Service untuk alur bisnis Pemeriksaan.

    Tanggung jawab:
    - Generate id_pemeriksaan
    - Validasi FK: Korban dan Tenaga Medis harus ada
    - Konversi status_triase string -> StatusTriase (Enum)
    - Membuat object Pemeriksaan
    - Menyimpan ke repository Pemeriksaan
    - (Opsional) Sinkron status triase korban setelah pemeriksaan
    """

    def __init__(
        self,
        pemeriksaan_repo: BaseRepository,
        korban_repo: BaseRepository,
        tenaga_medis_repo: BaseRepository,
        orang_repo: BaseRepository,
    ):
        """
        Inisialisasi PemeriksaanService.

        Args:
            pemeriksaan_repo (BaseRepository): Repository Pemeriksaan.
            korban_repo (BaseRepository): Repository Korban.
            tenaga_medis_repo (BaseRepository): Repository Tenaga Medis.
            orang_repo (BaseRepository): Repository Orang (untuk sinkron Korban sebagai Orang).
        """
        self._pemeriksaan_repo = pemeriksaan_repo
        self._korban_repo = korban_repo
        self._tenaga_medis_repo = tenaga_medis_repo
        self._orang_repo = orang_repo
        self._logger = get_logger(__name__)

    # ===== CREATE =====
    def buat_pemeriksaan(
        self,
        id_korban: str,
        id_tenaga_medis: str,
        keluhan: str,
        diagnosa: str,
        status_triase: str,
        tanggal_pemeriksaan: date | None = None,
        sinkron_triase_korban: bool = True,
    ) -> str:
        """
        Membuat pemeriksaan baru.

        Args:
            id_korban (str): ID korban (id_orang korban).
            id_tenaga_medis (str): ID tenaga medis (id_orang tenaga medis).
            keluhan (str): Keluhan korban.
            diagnosa (str): Diagnosa.
            status_triase (str): Status triase terbaru (string sesuai enum).
            tanggal_pemeriksaan (date | None): Jika None, diisi date.today().
            sinkron_triase_korban (bool): Jika True, status triase Korban ikut di-update.

        Returns:
            str: id_pemeriksaan yang dibuat.

        Raises:
            ValueError: Jika FK tidak ditemukan / enum tidak valid.
            RuntimeError: Jika penyimpanan gagal.
        """
        now = datetime.now()
        self._logger.info(f"Membuat pemeriksaan baru ({now})")

        # ===== FK: korban harus ada =====
        korban: Korban | None = self._korban_repo.ambil_berdasarkan_id(id_korban)
        if korban is None:
            raise ValueError("Korban tidak ditemukan")

        # ===== FK: tenaga medis harus ada =====
        tenaga_medis: TenagaMedis | None = self._tenaga_medis_repo.ambil_berdasarkan_id(id_tenaga_medis)
        if tenaga_medis is None:
            raise ValueError("Tenaga medis tidak ditemukan")

        # ===== tanggal default =====
        if tanggal_pemeriksaan is None:
            tanggal_pemeriksaan = date.today()

        # ===== parse triase =====
        triase_enum: StatusTriase = parse_enum(StatusTriase, status_triase)

        # ===== buat object pemeriksaan =====
        id_pemeriksaan = generate_id()
        pemeriksaan = Pemeriksaan(
            id_pemeriksaan=id_pemeriksaan,
            tenaga_medis=tenaga_medis,
            korban=korban,
            tanggal_pemeriksaan=tanggal_pemeriksaan,
            keluhan=keluhan,
            diagnosa=diagnosa,
            status_triase=triase_enum,
        )

        # ===== simpan pemeriksaan =====
        if not self._pemeriksaan_repo.tambah(pemeriksaan):
            self._logger.error(
                f"Gagal menyimpan pemeriksaan id_pemeriksaan={id_pemeriksaan} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan data pemeriksaan")

        # ===== opsional: sinkron triase korban =====
        if sinkron_triase_korban:
            korban.set_status_triase(triase_enum)

            # update di korban_repo dan orang_repo (karena korban juga tersimpan sebagai Orang)
            self._korban_repo.perbarui(id_korban, korban)
            self._orang_repo.perbarui(id_korban, korban)

            self._logger.info(
                f"Triase korban id_orang={id_korban} disinkron menjadi {triase_enum.value} ({datetime.now()})"
            )

        self._logger.info(
            f"Pemeriksaan id_pemeriksaan={id_pemeriksaan} berhasil dibuat ({datetime.now()})"
        )
        return id_pemeriksaan

    # ===== READ =====
    def ambil_pemeriksaan(self, id_pemeriksaan: str) -> Pemeriksaan | None:
        """
        Mengambil pemeriksaan berdasarkan id_pemeriksaan.
        """
        self._logger.info(
            f"Mengambil pemeriksaan id_pemeriksaan={id_pemeriksaan} ({datetime.now()})"
        )
        return self._pemeriksaan_repo.ambil_berdasarkan_id(id_pemeriksaan)

    def ambil_semua_pemeriksaan(self) -> list[Pemeriksaan]:
        """
        Mengambil semua data pemeriksaan.
        """
        self._logger.info(f"Mengambil semua pemeriksaan ({datetime.now()})")
        return self._pemeriksaan_repo.ambil_semua()

    # ===== UPDATE =====
    def perbarui_pemeriksaan(
        self,
        id_pemeriksaan: str,
        id_korban: str,
        id_tenaga_medis: str,
        tanggal_pemeriksaan: date,
        keluhan: str,
        diagnosa: str,
        status_triase: str,
        sinkron_triase_korban: bool = True,
    ) -> bool:
        """
        Memperbarui data pemeriksaan.
        """
        existing = self._pemeriksaan_repo.ambil_berdasarkan_id(id_pemeriksaan)
        if existing is None:
            self._logger.warning(
                f"Gagal update: pemeriksaan id_pemeriksaan={id_pemeriksaan} tidak ditemukan ({datetime.now()})"
            )
            return False

        korban = self._korban_repo.ambil_berdasarkan_id(id_korban)
        if korban is None:
            raise ValueError("Korban tidak ditemukan")

        tenaga_medis = self._tenaga_medis_repo.ambil_berdasarkan_id(id_tenaga_medis)
        if tenaga_medis is None:
            raise ValueError("Tenaga medis tidak ditemukan")

        triase_enum = parse_enum(StatusTriase, status_triase)

        pemeriksaan_baru = Pemeriksaan(
            id_pemeriksaan=id_pemeriksaan,
            tenaga_medis=tenaga_medis,
            korban=korban,
            tanggal_pemeriksaan=tanggal_pemeriksaan,
            keluhan=keluhan,
            diagnosa=diagnosa,
            status_triase=triase_enum,
        )

        sukses = self._pemeriksaan_repo.perbarui(id_pemeriksaan, pemeriksaan_baru)
        if sukses:
            self._logger.info(
                f"Pemeriksaan id_pemeriksaan={id_pemeriksaan} berhasil diperbarui ({datetime.now()})"
            )

            if sinkron_triase_korban:
                korban.set_status_triase(triase_enum)
                self._korban_repo.perbarui(id_korban, korban)
                self._orang_repo.perbarui(id_korban, korban)

        return sukses

    # ===== DELETE =====
    def hapus_pemeriksaan(self, id_pemeriksaan: str) -> bool:
        """
        Menghapus pemeriksaan berdasarkan id_pemeriksaan.
        """
        self._logger.info(
            f"Menghapus pemeriksaan id_pemeriksaan={id_pemeriksaan} ({datetime.now()})"
        )
        sukses = self._pemeriksaan_repo.hapus(id_pemeriksaan)

        if sukses:
            self._logger.info(
                f"Pemeriksaan id_pemeriksaan={id_pemeriksaan} berhasil dihapus ({datetime.now()})"
            )
        else:
            self._logger.warning(
                f"Gagal hapus: pemeriksaan id_pemeriksaan={id_pemeriksaan} tidak ditemukan ({datetime.now()})"
            )

        return sukses
