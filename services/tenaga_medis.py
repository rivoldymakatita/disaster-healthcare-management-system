from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id
from utils.enums.jenis_kelamin import JenisKelamin
from utils.enums.role_tenaga_medis import RoleTenagaMedis
from utils.enum_parser import parse_enum

from models.tenaga_medis import TenagaMedis
from models.posko import Posko
from repositories.base_repository import BaseRepository


class TenagaMedisService:
    """
    Service untuk alur bisnis Tenaga Medis.

    Tanggung jawab:
    - Generate id_orang
    - Konversi enum (jenis_kelamin, role)
    - Validasi FK ke Posko
    - Membuat object TenagaMedis (child dari Orang)
    - Menyimpan ke OrangRepository & TenagaMedisRepository
    """

    def __init__(
        self,
        tenaga_medis_repo: BaseRepository,
        orang_repo: BaseRepository,
        posko_repo: BaseRepository,
    ):
        """
        Inisialisasi TenagaMedisService.

        Args:
            tenaga_medis_repo (BaseRepository): Repository Tenaga Medis.
            orang_repo (BaseRepository): Repository Orang.
            posko_repo (BaseRepository): Repository Posko.
        """
        self._tenaga_medis_repo = tenaga_medis_repo
        self._orang_repo = orang_repo
        self._posko_repo = posko_repo
        self._logger = get_logger(__name__)

    # ===== CREATE =====
    def buat_tenaga_medis(
        self,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: str,
        tanggal_lahir_orang: date,
        id_posko: str,
        no_izin_praktik: str,
        role: str,
        spesialisasi: str,
    ) -> str:
        """
        Membuat Tenaga Medis baru.

        Args:
            nama_orang (str): Nama lengkap.
            alamat_orang (str): Alamat.
            jenis_kelamin_orang (str): Jenis kelamin (string sesuai enum).
            tanggal_lahir_orang (date): Tanggal lahir.
            id_posko (str): ID posko tempat bertugas.
            no_izin_praktik (str): Nomor izin praktik.
            role (str): Role tenaga medis (string sesuai enum).
            spesialisasi (str): Spesialisasi.

        Returns:
            str: id_orang tenaga medis yang dibuat.

        Raises:
            ValueError: Jika posko tidak ditemukan atau enum tidak valid.
            RuntimeError: Jika penyimpanan gagal.
        """
        self._logger.info(f"Membuat tenaga medis baru ({datetime.now()})")

        # ===== Validasi FK Posko =====
        posko: Posko | None = self._posko_repo.ambil_berdasarkan_id(id_posko)
        if posko is None:
            raise ValueError("Posko tidak ditemukan")

        # ===== Generate ID =====
        id_orang = generate_id()

        # ===== Parse Enum =====
        jk_enum: JenisKelamin = parse_enum(JenisKelamin, jenis_kelamin_orang)
        role_enum: RoleTenagaMedis = parse_enum(RoleTenagaMedis, role)

        tenaga_medis = TenagaMedis(
            id_orang=id_orang,
            nama_orang=nama_orang,
            alamat_orang=alamat_orang,
            jenis_kelamin_orang=jk_enum,
            tanggal_lahir_orang=tanggal_lahir_orang,
            posko=posko,
            no_izin_praktik=no_izin_praktik,
            role=role_enum,
            spesialisasi=spesialisasi,
        )

        # ===== Simpan ke OrangRepository =====
        if not self._orang_repo.tambah(tenaga_medis):
            self._logger.error(
                f"Gagal simpan Orang (TenagaMedis) id_orang={id_orang} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan data orang (Tenaga Medis)")

        # ===== Simpan ke TenagaMedisRepository =====
        if not self._tenaga_medis_repo.tambah(tenaga_medis):
            # rollback sederhana
            self._orang_repo.hapus(id_orang)
            self._logger.error(
                f"Gagal simpan TenagaMedis id_orang={id_orang} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan data tenaga medis")

        self._logger.info(
            f"TenagaMedis id_orang={id_orang} berhasil dibuat ({datetime.now()})"
        )
        return id_orang

    # ===== READ =====
    def ambil_tenaga_medis(self, id_orang: str) -> TenagaMedis | None:
        """
        Mengambil Tenaga Medis berdasarkan id_orang.
        """
        self._logger.info(
            f"Mengambil tenaga medis id_orang={id_orang} ({datetime.now()})"
        )
        return self._tenaga_medis_repo.ambil_berdasarkan_id(id_orang)

    def ambil_semua_tenaga_medis(self) -> list[TenagaMedis]:
        """
        Mengambil semua data Tenaga Medis.
        """
        self._logger.info(f"Mengambil semua tenaga medis ({datetime.now()})")
        return self._tenaga_medis_repo.ambil_semua()

    # ===== UPDATE =====
    def perbarui_tenaga_medis(
        self,
        id_orang: str,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: str,
        tanggal_lahir_orang: date,
        id_posko: str,
        no_izin_praktik: str,
        role: str,
        spesialisasi: str,
    ) -> bool:
        """
        Memperbarui data Tenaga Medis.
        """
        existing = self._tenaga_medis_repo.ambil_berdasarkan_id(id_orang)
        if existing is None:
            self._logger.warning(
                f"Gagal update: tenaga medis id_orang={id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        posko = self._posko_repo.ambil_berdasarkan_id(id_posko)
        if posko is None:
            raise ValueError("Posko tidak ditemukan")

        jk_enum = parse_enum(JenisKelamin, jenis_kelamin_orang)
        role_enum = parse_enum(RoleTenagaMedis, role)

        tenaga_medis_baru = TenagaMedis(
            id_orang=id_orang,
            nama_orang=nama_orang,
            alamat_orang=alamat_orang,
            jenis_kelamin_orang=jk_enum,
            tanggal_lahir_orang=tanggal_lahir_orang,
            posko=posko,
            no_izin_praktik=no_izin_praktik,
            role=role_enum,
            spesialisasi=spesialisasi,
        )

        sukses_orang = self._orang_repo.perbarui(id_orang, tenaga_medis_baru)
        sukses_tm = self._tenaga_medis_repo.perbarui(id_orang, tenaga_medis_baru)

        if sukses_orang and sukses_tm:
            self._logger.info(
                f"TenagaMedis id_orang={id_orang} berhasil diperbarui ({datetime.now()})"
            )
            return True

        self._logger.warning(
            f"Gagal update sebagian tenaga medis id_orang={id_orang} ({datetime.now()})"
        )
        return False

    # ===== DELETE =====
    def hapus_tenaga_medis(self, id_orang: str) -> bool:
        """
        Menghapus Tenaga Medis.
        """
        self._logger.info(
            f"Menghapus tenaga medis id_orang={id_orang} ({datetime.now()})"
        )

        sukses_tm = self._tenaga_medis_repo.hapus(id_orang)
        sukses_orang = self._orang_repo.hapus(id_orang)

        if sukses_tm and sukses_orang:
            self._logger.info(
                f"TenagaMedis id_orang={id_orang} berhasil dihapus ({datetime.now()})"
            )
            return True

        self._logger.warning(
            f"Gagal hapus tenaga medis id_orang={id_orang} ({datetime.now()})"
        )
        return False
