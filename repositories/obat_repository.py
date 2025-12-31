from datetime import datetime
from utils.loggers import get_logger
from base_repository import BaseRepository

class ObatRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data obat.

    Menyimpan objek Obat di dalam dictionary (key: id_obat).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_obat, value: Obat
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek obat ke repository.

        Args:
            data (Obat): Objek Obat yang akan ditambahkan.

        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada).
        """
        id_obat = data.get_id_obat()

        if id_obat in self._data:
            self.logger.warning(
                f"Obat ID {id_obat} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_obat] = data
        self.logger.info(
            f"Obat ID {id_obat} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_obat):
        """Mengambil obat berdasarkan ID.

        Args:
            id_obat (str): ID unik obat.
        Returns:
            Obat | None: Objek Obat jika ditemukan, None jika tidak.
        """
        obat = self._data.get(id_obat)
        if obat is None:
            self.logger.warning(
                f"Obat ID {id_obat} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"Obat ID {id_obat} berhasil diambil ({datetime.now()})"
            )

        return obat

    def ambil_semua(self):
        """Mengambil semua data obat.

        Returns:
            list[Obat]: Daftar semua objek Obat.
        """
        self.logger.info(
            f"Mengambil semua obat (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_obat, data):
        """Memperbarui obat berdasarkan ID.

        Args:
            id_obat (str): ID unik obat yang akan diperbarui.
            data (Obat): Data Obat baru.

        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_obat not in self._data:
            self.logger.warning(
                f"Gagal update: Obat ID {id_obat} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_obat] = data
        self.logger.info(
            f"Obat ID {id_obat} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_obat):
        """Menghapus obat berdasarkan ID.

        Args:
            id_obat (str): ID unik obat yang akan dihapus.
        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_obat not in self._data:
            self.logger.warning(
                f"Gagal hapus: Obat ID {id_obat} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_obat]
        self.logger.info(
            f"Obat ID {id_obat} berhasil dihapus ({datetime.now()})"
        )
        return True