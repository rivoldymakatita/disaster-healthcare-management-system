from datetime import datetime
from utils.loggers import get_logger
from .base_repository import BaseRepository


class BencanaRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk mengelola data bencana.

    Menyimpan objek Bencana di dalam dictionary (key: id_bencana).
    """

    def __init__(self):
        """Inisialisasi repository in-memory."""
        self._data = {}  # key: id_bencana, value: Bencana
        self.logger = get_logger(__name__)

    # ====== OVERRIDING METHOD DARI BaseRepository (Polymorphism) ======

    def tambah(self, data):
        """Menambahkan objek bencana ke repository."""
        id_bencana = data.get_id_bencana()

        if id_bencana in self._data:
            self.logger.warning(
                f"Bencana ID {id_bencana} sudah ada ({datetime.now()})"
            )
            return False

        self._data[id_bencana] = data
        self.logger.info(
            f"Bencana ID {id_bencana} berhasil ditambahkan ({datetime.now()})"
        )
        return True

    def ambil_berdasarkan_id(self, id_bencana):
        """Mengambil bencana berdasarkan ID."""
        bencana = self._data.get(id_bencana)

        if bencana is None:
            self.logger.warning(
                f"Bencana ID {id_bencana} tidak ditemukan ({datetime.now()})"
            )
        else:
            self.logger.info(
                f"Bencana ID {id_bencana} berhasil diambil ({datetime.now()})"
            )

        return bencana

    def ambil_semua(self):
        """Mengambil semua data bencana."""
        self.logger.info(
            f"Mengambil semua bencana (jumlah={len(self._data)}) ({datetime.now()})"
        )
        return list(self._data.values())

    def perbarui(self, id_bencana, data):
        """Memperbarui bencana berdasarkan ID."""
        if id_bencana not in self._data:
            self.logger.warning(
                f"Gagal update: Bencana ID {id_bencana} tidak ditemukan ({datetime.now()})"
            )
            return False

        self._data[id_bencana] = data
        self.logger.info(
            f"Bencana ID {id_bencana} berhasil diperbarui ({datetime.now()})"
        )
        return True

    def hapus(self, id_bencana):
        """Menghapus bencana berdasarkan ID."""
        if id_bencana not in self._data:
            self.logger.warning(
                f"Gagal hapus: Bencana ID {id_bencana} tidak ditemukan ({datetime.now()})"
            )
            return False

        del self._data[id_bencana]
        self.logger.info(
            f"Bencana ID {id_bencana} berhasil dihapus ({datetime.now()})"
        )
        return True
