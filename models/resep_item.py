from .obat import Obat


class ResepItem:
    """
    Merepresentasikan satu item obat dalam resep.

    Attributes:
        obat (Obat): Objek obat.
        qty (int): Jumlah obat yang diberikan.
        aturan_pakai (str): Aturan pakai obat.
        dosis (int): Dosis obat (positif).
    """

    def __init__(self, obat: Obat, qty: int, aturan_pakai: str, dosis: int):
        """
        Inisialisasi objek ResepItem.

        Args:
            obat (Obat): Objek obat.
            qty (int): Jumlah obat yang diberikan.
            aturan_pakai (str): Aturan pakai obat.
            dosis (int): Dosis obat (positif).

        Raises:
            ValueError: Jika salah satu argumen tidak valid.
        """
        self.set_obat(obat)
        self.set_qty(qty)
        self.set_aturan_pakai(aturan_pakai)
        self.set_dosis(dosis)

    # ===== Getter =====
    def get_obat(self) -> Obat:
        """
        Mengambil objek obat.

        Returns:
            Obat: Objek obat.
        """
        return self.__obat

    def get_qty(self) -> int:
        """
        Mengambil jumlah obat.

        Returns:
            int: Jumlah obat.
        """
        return self.__qty

    def get_aturan_pakai(self) -> str:
        """
        Mengambil aturan pakai obat.

        Returns:
            str: Aturan pakai obat.
        """
        return self.__aturan_pakai

    def get_dosis(self) -> int:
        """
        Mengambil dosis obat.

        Returns:
            int: Dosis obat.
        """
        return self.__dosis

    # ===== Setter =====
    def set_obat(self, obat: Obat) -> None:
        """
        Mengatur objek obat.

        Args:
            obat (Obat): Objek obat.

        Raises:
            ValueError: Jika obat bukan instance dari Obat.
        """
        if not isinstance(obat, Obat):
            raise ValueError("Obat tidak valid")
        self.__obat = obat

    def set_qty(self, qty: int) -> None:
        """
        Mengatur jumlah obat.

        Args:
            qty (int): Jumlah obat.

        Raises:
            ValueError: Jika qty bukan integer positif.
        """
        if not isinstance(qty, int) or qty <= 0:
            raise ValueError("Qty harus berupa integer positif")
        self.__qty = qty

    def set_aturan_pakai(self, aturan_pakai: str) -> None:
        """
        Mengatur aturan pakai obat.

        Args:
            aturan_pakai (str): Aturan pakai obat.

        Raises:
            ValueError: Jika aturan_pakai kosong atau bukan string.
        """
        if not isinstance(aturan_pakai, str) or not aturan_pakai.strip():
            raise ValueError("Aturan pakai tidak boleh kosong")
        self.__aturan_pakai = aturan_pakai

    def set_dosis(self, dosis: int) -> None:
        """
        Mengatur dosis obat.

        Args:
            dosis (int): Dosis obat.

        Raises:
            ValueError: Jika dosis bukan integer positif.
        """
        if not isinstance(dosis, int) or dosis <= 0:
            raise ValueError("Dosis harus berupa integer positif")
        self.__dosis = dosis
