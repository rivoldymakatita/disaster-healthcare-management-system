from datetime import datetime
from utils.loggers import get_logger
from base_repository import BaseRepository

class PoskoRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data posko.

    Menyimpan objek Posko di dalam dictionary (key: id_posko).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_posko, value: Posko
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek posko ke repository.

        Args:
            data (Posko): Objek Posko yang akan ditambahkan.

        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada).
        """
        id_posko = data.get_id_posko()

        if id_posko in self._data:
            self.logger.warning(
                f"Posko ID {id_posko} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_posko] = data
        self.logger.info(
            f"Posko ID {id_posko} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_posko):
        """Mengambil posko berdasarkan ID.

        Args:
            id_posko (str): ID unik posko.
        Returns:
            Posko | None: Objek Posko jika ditemukan, None jika tidak.
        """
        posko = self._data.get(id_posko)
        if posko is None:
            self.logger.warning(
                f"Posko ID {id_posko} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"Posko ID {id_posko} berhasil diambil ({datetime.now()})"
            )

        return posko

    def ambil_semua(self):
        """Mengambil semua data posko.

        Returns:
            list[Posko]: Daftar semua objek Posko.
        """
        self.logger.info(
            f"Mengambil semua posko (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_posko, data):
        """Memperbarui posko berdasarkan ID.

        Args:
            id_posko (str): ID unik posko yang akan diperbarui.
            data (Posko): Data Posko baru.

        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_posko not in self._data:
            self.logger.warning(
                f"Gagal update: Posko ID {id_posko} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_posko] = data
        self.logger.info(
            f"Posko ID {id_posko} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_posko):
        """Menghapus posko berdasarkan ID.

        Args:
            id_posko (str): ID unik posko yang akan dihapus.
        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_posko not in self._data:
            self.logger.warning(
                f"Gagal hapus: Posko ID {id_posko} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_posko]
        self.logger.info(
            f"Posko ID {id_posko} berhasil dihapus ({datetime.now()})"
        )
        return True