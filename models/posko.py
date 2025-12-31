from utils.enums.status_posko import StatusPosko
from bencana import Bencana

class Posko:
    """
    Kelas untuk merepresentasikan posko penanganan bencana.

    Attributes:
        id_posko (str): ID unik posko.
        bencana (Bencana): Bencana terkait posko.
        nama_posko (str): Nama posko.
        alamat_posko (str): Alamat posko.
        kapasitas_posko (int): Kapasitas posko.
        status_posko (StatusPosko): Status posko.
    """

    def __init__(self, id_posko: str, bencana: Bencana, nama_posko: str, alamat_posko: str, kapasitas_posko: int, status_posko: StatusPosko):
        """Inisialisasi objek Posko.

        Args:
            id_posko (str): ID unik posko.
            bencana (Bencana): Bencana terkait posko.
            nama_posko (str): Nama posko.
            alamat_posko (str): Alamat posko.
            kapasitas_posko (int): Kapasitas posko.
            status_posko (StatusPosko): Status posko.
        """
        self.set_id_posko(id_posko)
        self.set_bencana(bencana)
        self.set_nama_posko(nama_posko)
        self.set_alamat_posko(alamat_posko)
        self.set_kapasitas_posko(kapasitas_posko)
        self.set_status_posko(status_posko)

    # ===== Getter =====
    def get_id_posko(self) -> str:
        """Mengembalikan ID posko.

        Returns:
            str: ID posko.
        """
        return self.__id_posko

    def get_bencana(self) -> Bencana:
        """Mengembalikan bencana terkait posko.

        Returns:
            Bencana: Bencana terkait posko.
        """
        return self.__bencana

    def get_nama_posko(self) -> str:
        """Mengembalikan nama posko.

        Returns:
            str: Nama posko.
        """
        return self.__nama_posko

    def get_alamat_posko(self) -> str:
        """Mengembalikan alamat posko.

        Returns:
            str: Alamat posko.
        """
        return self.__alamat_posko

    def get_kapasitas_posko(self) -> int:
        """Mengembalikan kapasitas posko.

        Returns:
            int: Kapasitas posko.
        """
        return self.__kapasitas_posko

    def get_status_posko(self) -> StatusPosko:
        """Mengembalikan status posko.

        Returns:
            StatusPosko: Status posko.
        """
        return self.__status_posko

    # ===== Setter =====
    def set_id_posko(self, id_posko: str) -> None:
        """Mengubah ID posko.

        Args:
            id_posko (str): ID posko baru.

        Raises:
            ValueError: Jika ID posko bukan string atau kosong.
        """
        if not isinstance(id_posko, str) or not id_posko.strip():
            raise ValueError("ID posko tidak boleh kosong")
        self.__id_posko = id_posko

    def set_bencana(self, bencana: Bencana) -> None:
        """Mengubah bencana terkait posko.

        Args:
            bencana (Bencana): Bencana baru.

        Raises:
            ValueError: Jika bencana tidak valid.
        """
        if not isinstance(bencana, Bencana):
            raise ValueError("Bencana tidak valid")
        self.__bencana = bencana

    def set_nama_posko(self, nama_posko: str) -> None:
        """Mengubah nama posko.

        Args:
            nama_posko (str): Nama posko baru.

        Raises:
            ValueError: Jika nama posko bukan string atau kosong.
        """
        if not isinstance(nama_posko, str) or not nama_posko.strip():
            raise ValueError("Nama posko tidak boleh kosong")
        self.__nama_posko = nama_posko

    def set_alamat_posko(self, alamat_posko: str) -> None:
        """Mengubah alamat posko.

        Args:
            alamat_posko (str): Alamat posko baru.

        Raises:
            ValueError: Jika alamat posko bukan string atau kosong.
        """
        if not isinstance(alamat_posko, str) or not alamat_posko.strip():
            raise ValueError("Alamat posko tidak boleh kosong")
        self.__alamat_posko = alamat_posko
        
    def set_kapasitas_posko(self, kapasitas_posko: int) -> None:
        """Mengubah kapasitas posko.

        Args:
            kapasitas_posko (int): Kapasitas posko baru.

        Raises:
            ValueError: Jika kapasitas posko bukan integer atau negatif.
        """
        if not isinstance(kapasitas_posko, int):
            raise ValueError("Kapasitas harus berupa angka (int)")
        if kapasitas_posko < 0:
            raise ValueError("Kapasitas posko tidak boleh negatif")
        self.__kapasitas_posko = kapasitas_posko

    def set_status_posko(self, status_posko: StatusPosko) -> None:
        """Mengubah status posko.

        Args:
            status_posko (StatusPosko): Status posko baru.

        Raises:
            ValueError: Jika status posko tidak valid.
        """
        if not isinstance(status_posko, StatusPosko):
            raise ValueError("Status posko tidak valid")
        self.__status_posko = status_posko