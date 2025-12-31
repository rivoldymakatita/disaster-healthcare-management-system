class PatientService:
    """
    Service untuk mengelola logika bisnis terkait pasien.
    """

    def __init__(self, patient_repository):
        self.__patient_repository = patient_repository

    def registrasi_pasien(self, pasien):
        if pasien is None:
            raise ValueError("Data pasien tidak valid")

        if self.__patient_repository.ambil_berdasarkan_id(pasien.get_id()):
            raise ValueError("Pasien dengan ID tersebut sudah terdaftar")

        self.__patient_repository.tambah(pasien)

    def ambil_pasien(self, id_pasien):
        pasien = self.__patient_repository.ambil_berdasarkan_id(id_pasien)
        if not pasien:
            raise ValueError("Pasien tidak ditemukan")
        return pasien

    def ambil_semua_pasien(self):
        return self.__patient_repository.ambil_semua()
