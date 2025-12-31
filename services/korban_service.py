from datetime import date, datetime

from utils.loggers import get_logger
from utils.generator_id import generate_id
from utils.enums.jenis_kelamin import JenisKelamin
from utils.enums.status_triase import StatusTriase
from utils.enum_parser import parse_enum

from models.korban import Korban
from models.posko import Posko
from models.orang import Orang

from repositories.base_repository import BaseRepository


class KorbanService:
    """
    Service untuk alur bisnis Korban.

    Tanggung jawab:
    - Generate id_orang
    - Konversi enum (jenis_kelamin, status_triase)
    - Validasi FK ke Posko
    - Membuat object Korban (child dari Orang)
    - Menyimpan ke OrangRepository & KorbanRepository
    """

    def __init__(
        self,
        korban_repo: BaseRepository,
        orang_repo: BaseRepository,
        posko_repo: BaseRepository,
    ):
        """
        Inisialisasi KorbanService.

        Args:
            korban_repo (BaseRepository): Repository Korban.
            orang_repo (BaseRepository): Repository Orang.
            posko_repo (BaseRepository): Repository Posko.
        """
        self._korban_repo = korban_repo
        self._orang_repo = orang_repo
        self._posko_repo = posko_repo
        self._logger = get_logger(__name__)

    # ===== CREATE =====
    def buat_korban(
        self,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: str,
        tanggal_lahir_orang: date,
        status_triase: str,
        kondisi_awal: str,
        lokasi_ditemukan: str,
        id_posko: str,
    ) -> str:
        """
        Membuat Korban baru.

        Returns:
            str: id_orang korban yang dibuat.
        """
        self._logger.info(f"Membuat korban baru ({datetime.now()})")

        # ===== Validasi FK Posko =====
        posko: Posko | None = self._posko_repo.ambil_berdasarkan_id(id_posko)
        if posko is None:
            raise ValueError("Posko tidak ditemukan")

        # ===== Generate ID =====
        id_orang = generate_id()

        # ===== Parse Enum =====
        jk_enum: JenisKelamin = parse_enum(JenisKelamin, jenis_kelamin_orang)
        triase_enum: StatusTriase = parse_enum(StatusTriase, status_triase)

        # ===== Buat object Korban (child Orang) =====
        korban = Korban(
            id_orang=id_orang,
            nama_orang=nama_orang,
            alamat_orang=alamat_orang,
            jenis_kelamin_orang=jk_enum,
            tanggal_lahir_orang=tanggal_lahir_orang,
            status_triase=triase_enum,
            kondisi_awal=kondisi_awal,
            lokasi_ditemukan=lokasi_ditemukan,
            posko=posko,
        )

        # ===== Simpan ke OrangRepository =====
        if not self._orang_repo.tambah(korban):
            self._logger.error(
                f"Gagal simpan Orang (Korban) id_orang={id_orang} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan data orang (Korban)")

        # ===== Simpan ke KorbanRepository =====
        if not self._korban_repo.tambah(korban):
            # rollback sederhana (opsional)
            self._orang_repo.hapus(id_orang)
            self._logger.error(
                f"Gagal simpan Korban id_orang={id_orang} ({datetime.now()})"
            )
            raise RuntimeError("Gagal menyimpan data korban")

        self._logger.info(
            f"Korban id_orang={id_orang} berhasil dibuat ({datetime.now()})"
        )
        return id_orang

    # ===== READ =====
    def ambil_korban(self, id_orang: str) -> Korban | None:
        """
        Mengambil Korban berdasarkan id_orang.
        """
        self._logger.info(
            f"Mengambil korban id_orang={id_orang} ({datetime.now()})"
        )
        return self._korban_repo.ambil_berdasarkan_id(id_orang)

    def ambil_semua_korban(self) -> list[Korban]:
        """
        Mengambil semua data Korban.
        """
        self._logger.info(f"Mengambil semua korban ({datetime.now()})")
        return self._korban_repo.ambil_semua()

    # ===== UPDATE =====
    def perbarui_korban(
        self,
        id_orang: str,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: str,
        tanggal_lahir_orang: date,
        status_triase: str,
        kondisi_awal: str,
        lokasi_ditemukan: str,
        id_posko: str,
    ) -> bool:
        """
        Memperbarui data Korban.
        """
        existing = self._korban_repo.ambil_berdasarkan_id(id_orang)
        if existing is None:
            self._logger.warning(
                f"Gagal update: korban id_orang={id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        posko = self._posko_repo.ambil_berdasarkan_id(id_posko)
        if posko is None:
            raise ValueError("Posko tidak ditemukan")

        jk_enum = parse_enum(JenisKelamin, jenis_kelamin_orang)
        triase_enum = parse_enum(StatusTriase, status_triase)

        korban_baru = Korban(
            id_orang=id_orang,
            nama_orang=nama_orang,
            alamat_orang=alamat_orang,
            jenis_kelamin_orang=jk_enum,
            tanggal_lahir_orang=tanggal_lahir_orang,
            status_triase=triase_enum,
            kondisi_awal=kondisi_awal,
            lokasi_ditemukan=lokasi_ditemukan,
            posko=posko,
        )

        sukses_orang = self._orang_repo.perbarui(id_orang, korban_baru)
        sukses_korban = self._korban_repo.perbarui(id_orang, korban_baru)

        if sukses_orang and sukses_korban:
            self._logger.info(
                f"Korban id_orang={id_orang} berhasil diperbarui ({datetime.now()})"
            )
            return True

        self._logger.warning(
            f"Gagal update sebagian korban id_orang={id_orang} ({datetime.now()})"
        )
        return False

    # ===== DELETE =====
    def hapus_korban(self, id_orang: str) -> bool:
        """
        Menghapus Korban.
        """
        self._logger.info(
            f"Menghapus korban id_orang={id_orang} ({datetime.now()})"
        )

        sukses_korban = self._korban_repo.hapus(id_orang)
        sukses_orang = self._orang_repo.hapus(id_orang)

        if sukses_korban and sukses_orang:
            self._logger.info(
                f"Korban id_orang={id_orang} berhasil dihapus ({datetime.now()})"
            )
            return True

        self._logger.warning(
            f"Gagal hapus korban id_orang={id_orang} ({datetime.now()})"
        )
        return False
