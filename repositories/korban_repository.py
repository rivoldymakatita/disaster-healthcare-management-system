from datetime import datetime
from utils.loggers import get_logger
from .base_repository import BaseRepository

class KorbanRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data korban.

    Menyimpan objek Korban di dalam dictionary (key: id_orang).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_orang, value: Korban
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek korban ke repository.

        Args:
            data (Korban): Objek Korban yang akan ditambahkan.

        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada).
        """
        id_orang = data.get_id_orang()

        if id_orang in self._data:
            self.logger.warning(
                f"Korban ID {id_orang} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_orang] = data
        self.logger.info(
            f"Korban ID {id_orang} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_orang):
        """Mengambil korban berdasarkan ID.

        Args:
            id_orang (str): ID unik korban.
        Returns:
            Korban | None: Objek Korban jika ditemukan, None jika tidak.
        """
        korban = self._data.get(id_orang)
        if korban is None:
            self.logger.warning(
                f"Korban ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"Korban ID {id_orang} berhasil diambil ({datetime.now()})"
            )

        return korban

    def ambil_semua(self):
        """Mengambil semua data korban.

        Returns:
            list[Korban]: Daftar semua objek Korban.
        """
        self.logger.info(
            f"Mengambil semua korban (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_orang , data):
        """Memperbarui korban berdasarkan ID.

        Args:
            id_orang (str): ID unik korban yang akan diperbarui.
            data (Korban): Data Korban baru.

        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_orang not in self._data:
            self.logger.warning(
                f"Gagal update: Korban ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_orang] = data
        self.logger.info(
            f"Korban ID {id_orang} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_orang):
        """Menghapus korban berdasarkan ID.

        Args:
            id_orang (str): ID unik korban yang akan dihapus.
        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_orang not in self._data:
            self.logger.warning(
                f"Gagal hapus: Korban ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_orang]
        self.logger.info(
            f"Korban ID {id_orang} berhasil dihapus ({datetime.now()})"
        )
        return True