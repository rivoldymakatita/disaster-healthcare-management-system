from datetime import datetime
from utils.loggers import get_logger
from .base_repository import BaseRepository

class TenagaMedisRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data tenaga medis.

    Menyimpan objek TenagaMedis di dalam dictionary (key: id_orang).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_orang, value: TenagaMedis
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek tenaga medis ke repository.

        Args:
            data (TenagaMedis): Objek TenagaMedis yang akan ditambahkan.

        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada).
        """
        id_orang = data.get_id_orang()

        if id_orang in self._data:
            self.logger.warning(
                f"TenagaMedis ID {id_orang} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_orang] = data
        self.logger.info(
            f"TenagaMedis ID {id_orang} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_orang):
        """Mengambil tenaga medis berdasarkan ID.

        Args:
            id_orang (str): ID unik tenaga medis.
        Returns:
            TenagaMedis | None: Objek TenagaMedis jika ditemukan, None jika tidak.
        """
        tenaga_medis = self._data.get(id_orang)
        if tenaga_medis is None:
            self.logger.warning(
                f"TenagaMedis ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"TenagaMedis ID {id_orang} berhasil diambil ({datetime.now()})"
            )

        return tenaga_medis

    def ambil_semua(self):
        """Mengambil semua data tenaga medis.

        Returns:
            list[TenagaMedis]: Daftar semua objek TenagaMedis.
        """
        self.logger.info(
            f"Mengambil semua tenaga medis (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_orang, data):
        """Memperbarui tenaga medis berdasarkan ID.

        Args:
            id_orang (str): ID unik tenaga medis yang akan diperbarui.
            data (TenagaMedis): Data TenagaMedis baru.

        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_orang not in self._data:
            self.logger.warning(
                f"Gagal update: TenagaMedis ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_orang] = data
        self.logger.info(
            f"TenagaMedis ID {id_orang} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_orang):
        """Menghapus tenaga medis berdasarkan ID.

        Args:
            id_orang (str): ID unik tenaga medis yang akan dihapus.
        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_orang not in self._data:
            self.logger.warning(
                f"Gagal hapus: TenagaMedis ID {id_orang} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_orang]
        self.logger.info(
            f"TenagaMedis ID {id_orang} berhasil dihapus ({datetime.now()})"
        )
        return True