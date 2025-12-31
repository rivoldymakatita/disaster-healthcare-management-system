from datetime import date
from utils.enums.status_bencana import StatusBencana

class Bencana:

    """
    Class untuk merepresentasikan bencana dalam sistem penanganan kesehatan bencana.

    Attributes:
        bencana_id (str): ID unik untuk bencana.
        jenis (str): Jenis bencana (misalnya: gempa bumi, banjir, dll).
        lokasi (str): Lokasi terjadinya bencana.
        tanggal_mulai (date): Tanggal mulai terjadinya bencana.
        status (StatusBencana): Status terkini dari bencana.
    """

    def __init__(self, id_bencana: str, jenis: str, lokasi: str, tanggal_mulai: date, status: StatusBencana):
        self.set_id_bencana(id_bencana)
        self.set_jenis(jenis)
        self.set_lokasi(lokasi)
        self.set_tanggal_mulai(tanggal_mulai)
        self.set_status(status)

    # ===== Getter =====
    def get_id_bencana(self) -> str:

        """
        Mengembalikan ID bencana.

        Args:
            None

        Returns:
            str: ID bencana.
        """

        return self.__bencana_id

    def get_jenis(self) -> str:

        """
        Mengembalikan jenis bencana.
        
        Args:
            None
        
        Returns:
            str: Jenis bencana.
        """

        return self.__jenis

    def get_lokasi(self) -> str:
        
        """
        Mengembalikan lokasi bencana.

        Args:
            None
        
        Returns:
            str: Lokasi bencana.

        """

        return self.__lokasi

    def get_tanggal_mulai(self) -> date:
        
        """
        Mengembalikan tanggal mulai bencana.

        Args:
            None
        
        Returns:
            date: Tanggal mulai bencana.
        """

        return self.__tanggal_mulai

    def get_status(self) -> StatusBencana:

        """
        Mengembalikan status bencana.

        Args:
            None
        
        Returns:
            StatusBencana: Status bencana.
        """

        return self.__status

    # ===== Setter =====
    def set_id_bencana(self, id_bencana: str) -> None:

        """
        Mengubah ID bencana.

        Args:
            bencana_id (str): ID bencana baru.
        
        Returns:
            None
        
        Raises:
            ValueError: Jika ID bencana bukan string atau kosong.
        """

        if not isinstance(id_bencana, str) or not id_bencana.strip():
            raise ValueError("ID bencana tidak boleh kosong")
        self.__bencana_id = id_bencana

    def set_jenis(self, jenis: str) -> None:

        """
        Mengubah jenis bencana.

        Args:
            jenis (str): Jenis bencana baru.

        Returns:
            None
        
        Raises:
            ValueError: Jika jenis bukan string atau kosong.
        """

        if not isinstance(jenis, str) or not jenis.strip():
            raise ValueError("Jenis bencana tidak boleh kosong")
        self.__jenis = jenis

    def set_lokasi(self, lokasi: str) -> None:

        """
        Mengubah lokasi bencana.

        Args:
            lokasi (str): Lokasi bencana baru.

        Returns:
            None
        
        Raises:
            ValueError: Jika lokasi bukan string atau kosong.
        """

        if not isinstance(lokasi, str) or not lokasi.strip():
            raise ValueError("Lokasi bencana tidak boleh kosong")
        self.__lokasi = lokasi

    def set_tanggal_mulai(self, tanggal_mulai: date) -> None:

        """
        Mengubah tanggal mulai bencana.

        Args:
            tanggal_mulai (date): Tanggal mulai bencana baru.

        Returns:
            None

        Raises:
            ValueError: Jika tanggal mulai bukan date atau di masa depan.
        """

        if not isinstance(tanggal_mulai, date):
            raise ValueError("Tanggal mulai harus bertipe date")
        if tanggal_mulai > date.today():
            raise ValueError("Tanggal mulai tidak boleh di masa depan")
        self.__tanggal_mulai = tanggal_mulai

    def set_status(self, status: StatusBencana) -> None:
        
        """
        Mengubah status bencana.

        Args:
            status (StatusBencana): Status bencana baru.
        
        Returns:
            None

        Raises:
            ValueError: Jika status bencana tidak valid.
        """
        
        if not isinstance(status, StatusBencana):
            raise ValueError("Status bencana tidak valid")
        self.__status = status
