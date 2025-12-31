from datetime import date
from .orang import Orang
from utils.enums.jenis_kelamin import JenisKelamin
from utils.enums.status_triase import StatusTriase
from posko import Posko


class Korban(Orang):
    """
    Class untuk merepresentasikan pasien/korban bencana.
    Turunan dari class Orang.

    Attributes:
        id_orang (str): ID unik untuk orang.
        nama_orang (str): Nama lengkap orang.
        alamat_orang (str): Alamat tempat tinggal orang.
        jenis_kelamin_orang (JenisKelamin): Jenis kelamin orang.
        tanggal_lahir_orang (date): Tanggal lahir orang.
        status_triase (StatusTriase): Status triase korban.
        kondisi_awal (str): Kondisi awal korban saat ditemukan.
        lokasi_ditemukan (str): Lokasi dimana korban ditemukan.
        posko (Posko): Posko tempat korban ditangani.
    """

    def __init__(
        self,
        id_orang: str,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: JenisKelamin,
        tanggal_lahir_orang: date,
        status_triase: StatusTriase,
        kondisi_awal: str,
        lokasi_ditemukan: str,
        posko: Posko
    ):
        """Inisialisasi objek Korban.

        Args:
            id_orang (str): ID unik untuk orang.
            nama_orang (str): Nama lengkap orang.
            alamat_orang (str): Alamat tempat tinggal orang.
            jenis_kelamin_orang (JenisKelamin): Jenis kelamin orang.
            tanggal_lahir_orang (date): Tanggal lahir orang.
            status_triase (StatusTriase): Status triase korban.
            kondisi_awal (str): Kondisi awal korban saat ditemukan.
            lokasi_ditemukan (str): Lokasi dimana korban ditemukan.
            posko (Posko): Posko tempat korban ditangani.
        """
        super().__init__(id_orang, nama_orang, alamat_orang, jenis_kelamin_orang, tanggal_lahir_orang)
        self.set_status_triase(status_triase)
        self.set_kondisi_awal(kondisi_awal)
        self.set_lokasi_ditemukan(lokasi_ditemukan)
        self.set_posko(posko)

    # ===== Polymorphism (Override) =====
    def get_peran(self) -> str:
        """Mengembalikan peran orang.

        Returns:
            str: Peran orang.
        """
        return "Korban"

    # ===== Getter =====
    def get_posko(self) -> Posko:
        """Mengembalikan posko korban.

        Returns:
            Posko: Posko korban.
        """
        return self.__posko

    def get_status_triase(self) -> StatusTriase:
        """Mengembalikan status triase korban.

        Returns:
            StatusTriase: Status triase korban.
        """
        return self.__status_triase

    def get_kondisi_awal(self) -> str:
        """Mengembalikan kondisi awal korban.

        Returns:
            str: Kondisi awal korban.
        """
        return self.__kondisi_awal

    def get_lokasi_ditemukan(self) -> str:
        """Mengembalikan lokasi ditemukan korban.

        Returns:
            str: Lokasi ditemukan korban.
        """
        return self.__lokasi_ditemukan

    # ===== Setter =====
    def set_posko(self, posko: Posko) -> None:
        """Mengubah posko korban.

        Args:
            posko (Posko): Posko baru korban.

        Raises:
            ValueError: Jika posko tidak valid.
        """
        if not isinstance(posko, Posko):
            raise ValueError("Posko tidak valid")
        self.__posko = posko

    def set_status_triase(self, status_triase: StatusTriase) -> None:
        """Mengubah status triase korban.

        Args:
            status_triase (StatusTriase): Status triase baru korban.

        Raises:
            ValueError: Jika status triase tidak valid.
        """
        if not isinstance(status_triase, StatusTriase):
            raise ValueError("Status triase tidak valid")
        self.__status_triase = status_triase

    def set_kondisi_awal(self, kondisi_awal: str) -> None:
        """Mengubah kondisi awal korban.

        Args:
            kondisi_awal (str): Kondisi awal baru korban.

        Raises:
            ValueError: Jika kondisi awal tidak valid.
        """
        if not isinstance(kondisi_awal, str) or not kondisi_awal.strip():
            raise ValueError("Kondisi awal tidak boleh kosong")
        self.__kondisi_awal = kondisi_awal

    def set_lokasi_ditemukan(self, lokasi_ditemukan: str) -> None:
        """Mengubah lokasi ditemukan korban.

        Args:
            lokasi_ditemukan (str): Lokasi ditemukan baru korban.

        Raises:
            ValueError: Jika lokasi ditemukan tidak valid.
        """
        if not isinstance(lokasi_ditemukan, str) or not lokasi_ditemukan.strip():
            raise ValueError("Lokasi ditemukan tidak boleh kosong")
        self.__lokasi_ditemukan = lokasi_ditemukan
