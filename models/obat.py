from datetime import date

class Obat:

    """
    Class untuk merepresentasikan obat dalam sistem penanganan kesehatan bencana.

    Attributes:
        id_obat (str): ID unik untuk obat.
        nama_obat (str): Nama obat.
        stock_obat (int): Jumlah stock obat yang tersedia.
        satuan_obat (str): Satuan dari obat (misalnya: tablet, botol, dll).
        tanggal_kadaluarsa_obat (date): Tanggal kadaluarsa obat.
    """
    
    def __init__(
        self,
        id_obat: str,
        nama_obat: str,
        stock_obat: int,
        satuan_obat: str,
        tanggal_kadaluarsa_obat: date,
    ):
        """Inisialisasi objek Obat.

        Args:
            id_obat (str): ID unik untuk obat.
            nama_obat (str): Nama obat.
            stock_obat (int): Jumlah stock obat yang tersedia.
            satuan_obat (str): Satuan dari obat.
            tanggal_kadaluarsa_obat (date): Tanggal kadaluarsa obat.
        """
        self.set_id_obat(id_obat)
        self.set_nama_obat(nama_obat)
        self.set_stock_obat(stock_obat)
        self.set_satuan_obat(satuan_obat)
        self.set_tanggal_kadaluarsa_obat(tanggal_kadaluarsa_obat)

    # ===== Getter =====
    def get_id_obat(self) -> str:

        """
        Mengembalikan ID obat.

        Returns:
            str: ID obat.
        """
       
        return self.__id_obat
    
    def get_nama_obat(self) -> str:

        """
        Mengembalikan nama obat.

        Returns:
            str: Nama obat.
        """

        return self.__nama_obat

    def get_stock_obat(self) -> int:
        """
        Mengembalikan stock obat.

        Returns:
            int: Stock obat.
        """
        return self.__stock_obat
    
    def get_satuan_obat(self) -> str:

        """
        Mengembalikan satuan obat.

        Returns:
            str: Satuan obat.
        """

        return self.__satuan_obat
    
    def get_tanggal_kadaluarsa_obat(self) -> date:
        
        """
        Mengembalikan tanggal kadaluarsa obat.

        Returns:
            date: Tanggal kadaluarsa obat.
        """
        
        return self.__tanggal_kadaluarsa_obat
    
    # ===== Setter =====
    def set_id_obat(self, id_obat: str) -> None:
        """Mengubah ID obat.

        Args:
            id_obat (str): ID obat baru.

        Raises:
            ValueError: Jika ID obat bukan string atau kosong.
        """
        if not isinstance(id_obat, str) or not id_obat.strip():
            raise ValueError("ID obat tidak boleh kosong")
        self.__id_obat = id_obat

    def set_nama_obat(self, nama_obat: str) -> None:
        """Mengubah nama obat.

        Args:
            nama_obat (str): Nama obat baru.

        Raises:
            ValueError: Jika nama obat bukan string atau kosong.
        """
        if not isinstance(nama_obat, str) or not nama_obat.strip():
            raise ValueError("Nama obat tidak boleh kosong")
        self.__nama_obat = nama_obat

    def set_stock_obat(self, stock_obat: int) -> None:
        """Mengubah stock obat.

        Args:
            stock_obat (int): Stock obat baru.

        Raises:
            ValueError: Jika stock obat bukan integer atau kurang dari 0.
        """
        if not isinstance(stock_obat, int) or stock_obat < 0:
            raise ValueError("Stock obat harus berupa integer non-negatif")
        self.__stock_obat = stock_obat

    def set_satuan_obat(self, satuan_obat: str) -> None:
        """Mengubah satuan obat.

        Args:
            satuan_obat (str): Satuan obat baru.

        Raises:
            ValueError: Jika satuan obat bukan string atau kosong.
        """
        if not isinstance(satuan_obat, str) or not satuan_obat.strip():
            raise ValueError("Satuan obat tidak boleh kosong")
        self.__satuan_obat = satuan_obat

    def set_tanggal_kadaluarsa_obat(self, tanggal_kadaluarsa_obat: date) -> None:
        """Mengubah tanggal kadaluarsa obat.

        Args:
            tanggal_kadaluarsa_obat (date): Tanggal kadaluarsa obat baru.

        Raises:
            ValueError: Jika tanggal kadaluarsa bukan date atau di masa lalu.
        """
        if not isinstance(tanggal_kadaluarsa_obat, date):
            raise ValueError("Tanggal kadaluarsa harus bertipe date")
        if tanggal_kadaluarsa_obat < date.today():
            raise ValueError("Tanggal kadaluarsa tidak boleh di masa lalu")
        self.__tanggal_kadaluarsa_obat = tanggal_kadaluarsa_obat

