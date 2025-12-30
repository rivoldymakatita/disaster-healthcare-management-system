from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """
    Interface dasar untuk repository.
    """

    @abstractmethod
    def tambah(self, data):
        pass

    @abstractmethod
    def ambil_berdasarkan_id(self, data_id):
        pass

    @abstractmethod
    def ambil_semua(self):
        pass

    @abstractmethod
    def perbarui(self, data_id, data):
        pass

    @abstractmethod
    def hapus(self, data_id):
        pass
