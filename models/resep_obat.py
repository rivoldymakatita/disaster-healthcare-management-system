# src/models/resep_obat.py
from datetime import date
from .pemeriksaan import Pemeriksaan
from .resep_item import ResepItem


class ResepObat:
    """
    Merepresentasikan resep obat (header).

    Attributes:
        id_resep (str): ID unik resep.
        pemeriksaan (Pemeriksaan): Pemeriksaan terkait resep.
        items (list[ResepItem]): Daftar item obat dalam resep.
        tanggal_resep (date): Tanggal resep dibuat.
    """

    def __init__(
        self,
        id_resep: str,
        pemeriksaan: Pemeriksaan,
        items: list[ResepItem],
        tanggal_resep: date | None = None,
    ):
        """
        Inisialisasi objek ResepObat.

        Args:
            id_resep (str): ID unik resep.
            pemeriksaan (Pemeriksaan): Pemeriksaan terkait resep.
            items (list[ResepItem]): Daftar item obat dalam resep.
            tanggal_resep (date, optional): Tanggal resep dibuat. Default: hari ini.

        Raises:
            ValueError: Jika salah satu argumen tidak valid.
        """
        self.set_id_resep(id_resep)
        self.set_pemeriksaan(pemeriksaan)
        self.set_items(items)
        self.set_tanggal_resep(tanggal_resep or date.today())

    # ===== Getter =====
    def get_id_resep(self) -> str:
        """
        Mengambil ID resep.

        Returns:
            str: ID unik resep.
        """
        return self.__id_resep

    def get_pemeriksaan(self) -> Pemeriksaan:
        """
        Mengambil pemeriksaan terkait resep.

        Returns:
            Pemeriksaan: Pemeriksaan terkait resep.
        """
        return self.__pemeriksaan

    def get_items(self) -> list[ResepItem]:
        """
        Mengambil daftar item obat dalam resep.

        Returns:
            list[ResepItem]: Daftar item obat.
        """
        return list(self.__items)

    def get_tanggal_resep(self) -> date:
        """
        Mengambil tanggal resep dibuat.

        Returns:
            date: Tanggal resep dibuat.
        """
        return self.__tanggal_resep

    # ===== Setter =====
    def set_id_resep(self, id_resep: str) -> None:
        """
        Mengatur ID resep.

        Args:
            id_resep (str): ID unik resep.

        Raises:
            ValueError: Jika id_resep kosong atau bukan string.
        """
        if not isinstance(id_resep, str) or not id_resep.strip():
            raise ValueError("ID resep tidak boleh kosong")
        self.__id_resep = id_resep

    def set_pemeriksaan(self, pemeriksaan: Pemeriksaan) -> None:
        """
        Mengatur pemeriksaan terkait resep.

        Args:
            pemeriksaan (Pemeriksaan): Pemeriksaan terkait resep.

        Raises:
            ValueError: Jika pemeriksaan bukan instance Pemeriksaan.
        """
        if not isinstance(pemeriksaan, Pemeriksaan):
            raise ValueError("Pemeriksaan tidak valid")
        self.__pemeriksaan = pemeriksaan

    def set_items(self, items: list[ResepItem]) -> None:
        """
        Mengatur daftar item obat dalam resep.

        Args:
            items (list[ResepItem]): Daftar item obat.

        Raises:
            ValueError: Jika items kosong atau berisi objek bukan ResepItem.
        """
        if not isinstance(items, list) or len(items) == 0:
            raise ValueError("Items resep tidak boleh kosong")
        if not all(isinstance(item, ResepItem) for item in items):
            raise ValueError("Items harus berisi objek ResepItem")
        self.__items = list(items)

    def set_tanggal_resep(self, tanggal_resep: date) -> None:
        """
        Mengatur tanggal resep dibuat.

        Args:
            tanggal_resep (date): Tanggal resep dibuat.

        Raises:
            ValueError: Jika tanggal_resep bukan date atau di masa depan.
        """
        if not isinstance(tanggal_resep, date):
            raise ValueError("Tanggal resep harus bertipe date")
        if tanggal_resep > date.today():
            raise ValueError("Tanggal resep tidak boleh di masa depan")
        self.__tanggal_resep = tanggal_resep
