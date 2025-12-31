from abc import ABC, abstractmethod


class BaseRepository(ABC):
    """
    Interface dasar untuk seluruh repository.
    Bertindak sebagai kontrak CRUD umum.
    """

    @abstractmethod
    def tambah(self, data):
        """Menyimpan objek baru ke dalam repository.

        Args:
            data (object): Objek yang akan disimpan.

        Returns:
            bool: True jika berhasil, False jika gagal.
        """
        pass

    @abstractmethod
    def ambil_berdasarkan_id(self, data_id):
        """Mengambil satu objek berdasarkan ID.

        Args:
            data_id (str|int): ID data yang dicari.

        Returns:
            object: Objek yang ditemukan, None jika tidak ada.
        """
        pass

    @abstractmethod
    def ambil_semua(self):
        """Mengambil seluruh data yang tersimpan.

        Returns:
            list: Daftar seluruh objek dalam repository.
        """
        pass

    @abstractmethod
    def perbarui(self, data_id, data):
        """Memperbarui data berdasarkan ID.

        Args:
            data_id (str|int): ID data yang akan diperbarui.
            data (object): Data baru untuk memperbarui objek.

        Returns:
            bool: True jika berhasil, False jika gagal.
        """
        pass

    @abstractmethod
    def hapus(self, data_id):
        """Menghapus data berdasarkan ID.

        Args:
            data_id (str|int): ID data yang akan dihapus.

        Returns:
            bool: True jika berhasil, False jika gagal.
        """
        pass
