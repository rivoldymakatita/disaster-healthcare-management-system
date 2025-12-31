from datetime import date
from utils.enums.jenis_kelamin import JenisKelamin
from utils.enums.role_tenaga_medis import RoleTenagaMedis
from .orang import Orang
from .posko import Posko


class TenagaMedis(Orang):
    """
    Class untuk merepresentasikan tenaga medis
    dalam sistem penanganan kesehatan bencana.

    Attributes:
        id_orang (str): ID unik tenaga medis.
        nama_orang (str): Nama lengkap tenaga medis.
        alamat_orang (str): Alamat tempat tinggal tenaga medis.
        jenis_kelamin_orang (JenisKelamin): Jenis kelamin tenaga medis.
        tanggal_lahir_orang (date): Tanggal lahir tenaga medis.
        posko (Posko): Posko tempat bertugas.
        no_izin_praktik (str): Nomor izin praktik tenaga medis.
        role (RoleTenagaMedis): Peran tenaga medis.
        spesialisasi (str): Spesialisasi tenaga medis.
    """

    def __init__(
        self,
        id_orang: str,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: JenisKelamin,
        tanggal_lahir_orang: date,
        posko: Posko,
        no_izin_praktik: str,
        role: RoleTenagaMedis,
        spesialisasi: str
    ):
        """Inisialisasi objek TenagaMedis.

        Args:
            id_orang (str): ID unik tenaga medis.
            nama_orang (str): Nama lengkap tenaga medis.
            alamat_orang (str): Alamat tempat tinggal tenaga medis.
            jenis_kelamin_orang (JenisKelamin): Jenis kelamin tenaga medis.
            tanggal_lahir_orang (date): Tanggal lahir tenaga medis.
            posko (Posko): Posko tempat bertugas.
            no_izin_praktik (str): Nomor izin praktik tenaga medis.
            role (RoleTenagaMedis): Peran tenaga medis.
            spesialisasi (str): Spesialisasi tenaga medis.
        """
        super().__init__(id_orang, nama_orang, alamat_orang, jenis_kelamin_orang, tanggal_lahir_orang)
        self.set_posko(posko)
        self.set_no_izin_praktik(no_izin_praktik)
        self.set_role(role)
        self.set_spesialisasi(spesialisasi)

    # ===== Polymorphism (Override) =====
    def get_peran(self) -> str:
        """Mengembalikan peran orang.

        Returns:
            str: Peran orang.
        """
        return "Tenaga Medis"

    # ===== Getter =====
    def get_posko(self) -> Posko:
        """Mengembalikan posko tenaga medis.

        Returns:
            Posko: Posko tempat bertugas.
        """
        return self.__posko

    def get_no_izin_praktik(self) -> str:
        """Mengembalikan nomor izin praktik tenaga medis.

        Returns:
            str: Nomor izin praktik tenaga medis.
        """
        return self.__no_izin_praktik

    def get_role(self) -> RoleTenagaMedis:
        """Mengembalikan peran tenaga medis.

        Returns:
            RoleTenagaMedis: Peran tenaga medis.
        """
        return self.__role

    def get_spesialisasi(self) -> str:
        """Mengembalikan spesialisasi tenaga medis.

        Returns:
            str: Spesialisasi tenaga medis.
        """
        return self.__spesialisasi

    # ===== Setter =====
    def set_posko(self, posko: Posko) -> None:
        """Mengubah posko tenaga medis.

        Args:
            posko (Posko): Posko baru.

        Raises:
            ValueError: Jika posko tidak valid.
        """
        if not isinstance(posko, Posko):
            raise ValueError("Posko tidak valid")
        self.__posko = posko

    def set_no_izin_praktik(self, no_izin_praktik: str) -> None:
        """Mengubah nomor izin praktik tenaga medis.

        Args:
            no_izin_praktik (str): Nomor izin praktik baru.

        Raises:
            ValueError: Jika nomor izin praktik bukan string atau kosong.
        """
        if not isinstance(no_izin_praktik, str) or not no_izin_praktik.strip():
            raise ValueError("Nomor izin praktik tidak boleh kosong")
        self.__no_izin_praktik = no_izin_praktik

    def set_role(self, role: RoleTenagaMedis) -> None:
        """Mengubah peran tenaga medis.

        Args:
            role (RoleTenagaMedis): Peran tenaga medis baru.

        Raises:
            ValueError: Jika peran tenaga medis tidak valid.
        """
        if not isinstance(role, RoleTenagaMedis):
            raise ValueError("Peran tenaga medis tidak valid")
        self.__role = role

    def set_spesialisasi(self, spesialisasi: str) -> None:
        """Mengubah spesialisasi tenaga medis.

        Args:
            spesialisasi (str): Spesialisasi baru.

        Raises:
            ValueError: Jika spesialisasi bukan string atau kosong.
        """
        if not isinstance(spesialisasi, str) or not spesialisasi.strip():
            raise ValueError("Spesialisasi tidak boleh kosong")
        self.__spesialisasi = spesialisasi
