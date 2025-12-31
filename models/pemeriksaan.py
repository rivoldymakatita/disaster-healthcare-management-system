from datetime import date
from utils.enums.status_triase import StatusTriase
from .tenaga_medis import TenagaMedis
from .korban import Korban


class Pemeriksaan:
    """
    Kelas untuk merepresentasikan pemeriksaan medis.

    Attributes:
        id_pemeriksaan (str): ID unik pemeriksaan.
        tenaga_medis (TenagaMedis): Tenaga medis yang melakukan pemeriksaan.
        korban (Korban): Korban yang diperiksa.
        tanggal_pemeriksaan (date): Tanggal pemeriksaan.
        keluhan (str): Keluhan korban.
        diagnosa (str): Diagnosa hasil pemeriksaan.
        status_triase (StatusTriase): Status triase setelah pemeriksaan.
    """

    def __init__(
        self,
        id_pemeriksaan: str,
        tenaga_medis: TenagaMedis,
        korban: Korban,
        tanggal_pemeriksaan: date,
        keluhan: str,
        diagnosa: str,
        status_triase: StatusTriase,
    ):
        """Inisialisasi objek Pemeriksaan.

        Args:
            id_pemeriksaan (str): ID unik pemeriksaan.
            tenaga_medis (TenagaMedis): Tenaga medis yang melakukan pemeriksaan.
            korban (Korban): Korban yang diperiksa.
            tanggal_pemeriksaan (date): Tanggal pemeriksaan.
            keluhan (str): Keluhan korban.
            diagnosa (str): Diagnosa hasil pemeriksaan.
            status_triase (StatusTriase): Status triase setelah pemeriksaan.
        """
        self.set_id_pemeriksaan(id_pemeriksaan)
        self.set_tenaga_medis(tenaga_medis)
        self.set_korban(korban)
        self.set_tanggal_pemeriksaan(tanggal_pemeriksaan)
        self.set_keluhan(keluhan)
        self.set_diagnosa(diagnosa)
        self.set_status_triase(status_triase)

    # ===== Getter =====
    def get_id_pemeriksaan(self) -> str:
        """Mengembalikan ID pemeriksaan.

        Returns:
            str: ID pemeriksaan.
        """
        return self.__id_pemeriksaan

    def get_tenaga_medis(self) -> TenagaMedis:
        """Mengembalikan tenaga medis yang melakukan pemeriksaan.

        Returns:
            TenagaMedis: Tenaga medis pemeriksa.
        """
        return self.__tenaga_medis

    def get_korban(self) -> Korban:
        """Mengembalikan korban yang diperiksa.

        Returns:
            Korban: Korban yang diperiksa.
        """
        return self.__korban

    def get_tanggal_pemeriksaan(self) -> date:
        """Mengembalikan tanggal pemeriksaan.

        Returns:
            date: Tanggal pemeriksaan.
        """
        return self.__tanggal_pemeriksaan

    def get_keluhan(self) -> str:
        """Mengembalikan keluhan korban.

        Returns:
            str: Keluhan korban.
        """
        return self.__keluhan

    def get_diagnosa(self) -> str:
        """Mengembalikan diagnosa hasil pemeriksaan.

        Returns:
            str: Diagnosa hasil pemeriksaan.
        """
        return self.__diagnosa

    def get_status_triase(self) -> StatusTriase:
        """Mengembalikan status triase setelah pemeriksaan.

        Returns:
            StatusTriase: Status triase setelah pemeriksaan.
        """
        return self.__status_triase

    # ===== Setter =====
    def set_id_pemeriksaan(self, id_pemeriksaan: str) -> None:
        """Mengatur ID pemeriksaan.

        Args:
            id_pemeriksaan (str): ID pemeriksaan baru.

        Raises:
            ValueError: Jika ID pemeriksaan bukan string atau kosong.
        """
        if not isinstance(id_pemeriksaan, str) or not id_pemeriksaan.strip():
            raise ValueError("ID pemeriksaan tidak boleh kosong")
        self.__id_pemeriksaan = id_pemeriksaan

    def set_tenaga_medis(self, tenaga_medis: TenagaMedis) -> None:
        """Mengatur tenaga medis yang melakukan pemeriksaan.

        Args:
            tenaga_medis (TenagaMedis): Tenaga medis pemeriksa.

        Raises:
            ValueError: Jika tenaga medis tidak valid.
        """
        if not isinstance(tenaga_medis, TenagaMedis):
            raise ValueError("Tenaga medis tidak boleh kosong")
        self.__tenaga_medis = tenaga_medis

    def set_korban(self, korban: Korban) -> None:
        """Mengatur korban yang diperiksa.

        Args:
            korban (Korban): Korban yang diperiksa.

        Raises:
            ValueError: Jika korban tidak valid.
        """
        if not isinstance(korban, Korban):
            raise ValueError("Korban tidak boleh kosong")
        self.__korban = korban

    def set_tanggal_pemeriksaan(self, tanggal_pemeriksaan: date) -> None:
        """Mengatur tanggal pemeriksaan.

        Args:
            tanggal_pemeriksaan (date): Tanggal pemeriksaan baru.

        Raises:
            ValueError: Jika tanggal pemeriksaan bukan date atau di masa depan.
        """
        if not isinstance(tanggal_pemeriksaan, date):
            raise ValueError("Tanggal pemeriksaan harus bertipe date")
        if tanggal_pemeriksaan > date.today():
            raise ValueError("Tanggal pemeriksaan tidak boleh di masa depan")
        self.__tanggal_pemeriksaan = tanggal_pemeriksaan

    def set_keluhan(self, keluhan: str) -> None:
        """Mengatur keluhan korban.

        Args:
            keluhan (str): Keluhan korban.

        Raises:
            ValueError: Jika keluhan bukan string atau kosong.
        """
        if not isinstance(keluhan, str) or not keluhan.strip():
            raise ValueError("Keluhan tidak boleh kosong")
        self.__keluhan = keluhan

    def set_diagnosa(self, diagnosa: str) -> None:
        """Mengatur diagnosa hasil pemeriksaan.

        Args:
            diagnosa (str): Diagnosa hasil pemeriksaan.

        Raises:
            ValueError: Jika diagnosa bukan string atau kosong.
        """
        if not isinstance(diagnosa, str) or not diagnosa.strip():
            raise ValueError("Diagnosa tidak boleh kosong")
        self.__diagnosa = diagnosa

    def set_status_triase(self, status_triase: StatusTriase) -> None:
        """Mengatur status triase setelah pemeriksaan.

        Args:
            status_triase (StatusTriase): Status triase baru.

        Raises:
            ValueError: Jika status triase tidak valid.
        """
        if not isinstance(status_triase, StatusTriase):
            raise ValueError("Status triase tidak valid")
        self.__status_triase = status_triase
