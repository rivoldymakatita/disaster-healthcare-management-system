from abc import ABC, abstractmethod
from datetime import date
from utils.enums.jenis_kelamin import JenisKelamin 

class Orang(ABC):
    """
    Abstract base class untuk merepresentasikan manusia
    dalam sistem penanganan kesehatan bencana.
    """

    def __init__(
        self,
        id_orang: str,
        nama_orang: str,
        alamat_orang: str,
        jenis_kelamin_orang: JenisKelamin,
        tanggal_lahir_orang: date
    ):
        """Inisialisasi objek Orang.

        Args:
            id_orang (str): ID unik untuk orang.
            nama_orang (str): Nama lengkap orang.
            umur_orang (int): Umur orang.
            alamat_orang (str): Alamat tempat tinggal orang.
            jenis_kelamin_orang (JenisKelamin): Jenis kelamin orang.
            tanggal_lahir_orang (date): Tanggal lahir orang.
        """
        self.set_id_orang(id_orang)
        self.set_nama_orang(nama_orang)
        self.set_alamat_orang(alamat_orang)
        self.set_jenis_kelamin_orang(jenis_kelamin_orang)
        self.set_tanggal_lahir_orang(tanggal_lahir_orang)

    # ===== Getter =====
    def get_id_orang(self) -> str:
        """Mengembalikan ID orang.

        Returns:
            str: ID orang.
        """
        return self.__id_orang

    def get_nama_orang(self) -> str:
        """Mengembalikan nama orang.

        Returns:
            str: Nama orang.
        """
        return self.__nama_orang

    def get_alamat_orang(self) -> str:
        """Mengembalikan alamat orang.

        Returns:
            str: Alamat orang.
        """
        return self.__alamat_orang

    def get_jenis_kelamin_orang(self) -> JenisKelamin:
        """Mengembalikan jenis kelamin orang.

        Returns:
            JenisKelamin: Jenis kelamin orang.
        """
        return self.__jenis_kelamin_orang
    
    def get_tanggal_lahir_orang(self) -> date:
        """Mengembalikan tanggal lahir orang.

        Returns:
            date: Tanggal lahir orang.
        """
        return self.__tanggal_lahir_orang

    # ===== Setter =====
    def set_id_orang(self, id_orang: str) -> None:
        """Mengubah ID orang.

        Args:
            id_orang (str): ID orang baru.

        Raises:
            ValueError: Jika ID orang bukan string atau kosong.
        """
        if not isinstance(id_orang, str) or not id_orang.strip():
            raise ValueError("ID orang tidak boleh kosong")
        self.__id_orang = id_orang
        
    def set_nama_orang(self, nama_orang: str) -> None:
        """Mengubah nama orang.

        Args:
            nama_orang (str): Nama orang baru.

        Raises:
            ValueError: Jika nama orang bukan string atau kosong.
        """
        if not isinstance(nama_orang, str) or not nama_orang.strip():
            raise ValueError("Nama orang tidak boleh kosong")
        self.__nama_orang = nama_orang

    def set_alamat_orang(self, alamat_orang: str) -> None:
        """Mengubah alamat orang.

        Args:
            alamat_orang (str): Alamat orang baru.

        Raises:
            ValueError: Jika alamat bukan string atau kosong.
        """
        if not isinstance(alamat_orang, str) or not alamat_orang.strip():
            raise ValueError("Alamat tidak boleh kosong")
        self.__alamat_orang = alamat_orang

    def set_jenis_kelamin_orang(self, jenis_kelamin_orang: JenisKelamin) -> None:
        """Mengubah jenis kelamin orang.

        Args:
            jenis_kelamin_orang (JenisKelamin): Jenis kelamin orang baru.

        Raises:
            ValueError: Jika jenis kelamin tidak valid.
        """
        if not isinstance(jenis_kelamin_orang, JenisKelamin):
            raise ValueError("Jenis kelamin tidak valid")
        self.__jenis_kelamin_orang = jenis_kelamin_orang

    def set_tanggal_lahir_orang(self, tanggal_lahir_orang: date) -> None:
        """Mengubah tanggal lahir orang.

        Args:
            tanggal_lahir_orang (date): Tanggal lahir orang baru.

        Raises:
            ValueError: Jika tanggal lahir bukan date atau di masa depan.
        """
        if not isinstance(tanggal_lahir_orang, date):
            raise ValueError("Tanggal lahir harus bertipe date")
        if tanggal_lahir_orang > date.today():
            raise ValueError("Tanggal lahir tidak boleh di masa depan")
        self.__tanggal_lahir_orang = tanggal_lahir_orang

    # ===== Abstract Method (Polymorphism) =====
    @abstractmethod
    def get_peran(self) -> str:
        """Harus dioverride oleh child class.

        Returns:
            str: Peran orang (contoh: 'Korban', 'Tenaga Medis').
        """
        pass