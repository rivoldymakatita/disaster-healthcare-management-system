from repositories.base_repository import BaseRepository


class PatientRepository(BaseRepository):
    """
    Repository untuk mengelola data pasien.
    """

    def __init__(self):
        self.__data_pasien = {}

    def tambah(self, pasien):
        self.__data_pasien[pasien.get_id()] = pasien

    def ambil_berdasarkan_id(self, id_pasien):
        return self.__data_pasien.get(id_pasien)

    def ambil_semua(self):
        return list(self.__data_pasien.values())

    def perbarui(self, id_pasien, pasien):
        if id_pasien in self.__data_pasien:
            self.__data_pasien[id_pasien] = pasien
        else:
            raise ValueError("Pasien tidak ditemukan")

    def hapus(self, id_pasien):
        if id_pasien in self.__data_pasien:
            del self.__data_pasien[id_pasien]
        else:
            raise ValueError("Pasien tidak ditemukan")
