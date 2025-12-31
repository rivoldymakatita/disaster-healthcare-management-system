# src/repositories/resep_obat_repository_memory.py
from datetime import datetime
from utils.loggers import get_logger
from .base_repository import BaseRepository


class ResepObatRepositoryMemory(BaseRepository):
    """
    Repository in-memory untuk ResepObat.
    key: id_resep, value: ResepObat
    """

    def __init__(self):
        self._data = {}
        self.logger = get_logger(__name__)

    def tambah(self, data):
        id_resep = data.get_id_resep()
        if id_resep in self._data:
            self.logger.warning(f"Resep ID {id_resep} sudah ada ({datetime.now()})")
            return False
        self._data[id_resep] = data
        self.logger.info(f"Resep ID {id_resep} berhasil ditambahkan ({datetime.now()})")
        return True

    def ambil_berdasarkan_id(self, data_id):
        resep = self._data.get(data_id)
        if resep is None:
            self.logger.warning(f"Resep ID {data_id} tidak ditemukan ({datetime.now()})")
        else:
            self.logger.info(f"Resep ID {data_id} berhasil diambil ({datetime.now()})")
        return resep

    def ambil_semua(self):
        self.logger.info(f"Mengambil semua resep (jumlah={len(self._data)}) ({datetime.now()})")
        return list(self._data.values())

    def perbarui(self, data_id, data):
        if data_id not in self._data:
            self.logger.warning(f"Gagal update: Resep ID {data_id} tidak ditemukan ({datetime.now()})")
            return False
        self._data[data_id] = data
        self.logger.info(f"Resep ID {data_id} berhasil diperbarui ({datetime.now()})")
        return True

    def hapus(self, data_id):
        if data_id not in self._data:
            self.logger.warning(f"Gagal hapus: Resep ID {data_id} tidak ditemukan ({datetime.now()})")
            return False
        del self._data[data_id]
        self.logger.info(f"Resep ID {data_id} berhasil dihapus ({datetime.now()})")
        return True
