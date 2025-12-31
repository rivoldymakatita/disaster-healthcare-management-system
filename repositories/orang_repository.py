from datetime import datetime
from utils.loggers import get_logger
from .base_repository import BaseRepository

class OrangRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data orang.

    Menyimpan objek Orang di dalam dictionary (key: id_orang).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_orang, value: Orang
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek orang ke repository.

        Args:
            data (Orang): Objek Orang yang akan ditambahkan.

        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada).
        """
        id_orang = data.get_id_orang()

        if id_orang in self._data:
            self.logger.warning(
                f"Orang ID {id_orang} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_orang] = data
        self.logger.info(
            f"Orang ID {id_orang} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_orang):
        """Mengambil orang berdasarkan ID.

        Args:
            id_orang (str): ID unik orang.
        Returns:
            Orang | None: Objek Orang jika ditemukan, None jika tidak.
        """
        orang = self._data.get(id_orang)
        if orang is None:
            self.logger.warning(
                f"Orang ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"Orang ID {id_orang} berhasil diambil ({datetime.now()})"
            )

        return orang

    def ambil_semua(self):
        """Mengambil semua data orang.

        Returns:
            list[Orang]: Daftar semua objek Orang.
        """
        self.logger.info(
            f"Mengambil semua orang (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_orang, data):
        """Memperbarui orang berdasarkan ID.

        Args:
            id_orang (str): ID unik orang yang akan diperbarui.
            data (Orang): Data Orang baru.

        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_orang not in self._data:
            self.logger.warning(
                f"Gagal update: Orang ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_orang] = data
        self.logger.info(
            f"Orang ID {id_orang} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_orang):
        """Menghapus orang berdasarkan ID.

        Args:
            id_orang (str): ID unik orang yang akan dihapus.
        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_orang not in self._data:
            self.logger.warning(
                f"Gagal hapus: Orang ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_orang]
        self.logger.info(
            f"Orang ID {id_orang} berhasil dihapus ({datetime.now()})"
        )
        return True