from repositories.base_repository import BaseRepository


class MedicalRecordRepository(BaseRepository):
    """
    Repository untuk mengelola rekam medis pasien.
    """

    def __init__(self):
        self.__rekam_medis = {}

    def tambah(self, rekam_medis):
        self.__rekam_medis[rekam_medis.get_id()] = rekam_medis

    def ambil_berdasarkan_id(self, id_rekam_medis):
        return self.__rekam_medis.get(id_rekam_medis)

    def ambil_semua(self):
        return list(self.__rekam_medis.values())

    def perbarui(self, id_rekam_medis, rekam_medis):
        if id_rekam_medis in self.__rekam_medis:
            self.__rekam_medis[id_rekam_medis] = rekam_medis
        else:
            raise ValueError("Rekam medis tidak ditemukan")

    def hapus(self, id_rekam_medis):
        if id_rekam_medis in self.__rekam_medis:
            del self.__rekam_medis[id_rekam_medis]
        else:
            raise ValueError("Rekam medis tidak ditemukan")
