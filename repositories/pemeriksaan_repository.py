from datetime import datetime
from utils.loggers import get_logger
from base_repository import BaseRepository

class PemeriksaanRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data pemeriksaan.

    Menyimpan objek Pemeriksaan di dalam dictionary (key: id_pemeriksaan).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_pemeriksaan, value: Pemeriksaan
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek pemeriksaan ke repository.

        Args:
            data (Pemeriksaan): Objek Pemeriksaan yang akan ditambahkan.

        Returns:
            bool: True jika berhasil, False jika gagal (ID sudah ada).
        """
        id_pemeriksaan = data.get_id_pemeriksaan()

        if id_pemeriksaan in self._data:
            self.logger.warning(
                f"Pemeriksaan ID {id_pemeriksaan} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_pemeriksaan] = data
        self.logger.info(
            f"Pemeriksaan ID {id_pemeriksaan} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_pemeriksaan):
        """Mengambil pemeriksaan berdasarkan ID.

        Args:
            id_pemeriksaan (str): ID unik pemeriksaan.
        Returns:
            Pemeriksaan | None: Objek Pemeriksaan jika ditemukan, None jika tidak.
        """
        pemeriksaan = self._data.get(id_pemeriksaan)
        if pemeriksaan is None:
            self.logger.warning(
                f"Pemeriksaan ID {id_pemeriksaan} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"Pemeriksaan ID {id_pemeriksaan} berhasil diambil ({datetime.now()})"
            )

        return pemeriksaan

    def ambil_semua(self):
        """Mengambil semua data pemeriksaan.

        Returns:
            list[Pemeriksaan]: Daftar semua objek Pemeriksaan.
        """
        self.logger.info(
            f"Mengambil semua pemeriksaan (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_pemeriksaan, data):
        """Memperbarui pemeriksaan berdasarkan ID.

        Args:
            id_pemeriksaan (str): ID unik pemeriksaan yang akan diperbarui.
            data (Pemeriksaan): Data Pemeriksaan baru.

        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_pemeriksaan not in self._data:
            self.logger.warning(
                f"Gagal update: Pemeriksaan ID {id_pemeriksaan} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_pemeriksaan] = data
        self.logger.info(
            f"Pemeriksaan ID {id_pemeriksaan} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_pemeriksaan):
        """Menghapus pemeriksaan berdasarkan ID.

        Args:
            id_pemeriksaan (str): ID unik pemeriksaan yang akan dihapus.
        Returns:
            bool: True jika berhasil, False jika gagal (ID tidak ditemukan).
        """
        if id_pemeriksaan not in self._data:
            self.logger.warning(
                f"Gagal hapus: Pemeriksaan ID {id_pemeriksaan} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_pemeriksaan]
        self.logger.info(
            f"Pemeriksaan ID {id_pemeriksaan} berhasil dihapus ({datetime.now()})"
        )
        return True