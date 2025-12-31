class MedicalService:
    """
    Service untuk mengelola proses penanganan medis pasien.
    """

    def __init__(self, patient_repository, medical_record_repository):
        self.__patient_repository = patient_repository
        self.__medical_record_repository = medical_record_repository

    def proses_penanganan(self, id_pasien, rekam_medis):
        pasien = self.__patient_repository.ambil_berdasarkan_id(id_pasien)

        if not pasien:
            raise ValueError("Pasien tidak ditemukan")

        self.__medical_record_repository.tambah(rekam_medis)

        pasien.perbarui_status_kesehatan(rekam_medis.get_diagnosis())

        self.__patient_repository.perbarui(id_pasien, pasien)
