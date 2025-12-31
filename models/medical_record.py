from datetime import datetime
from .patient import Patient


class MedicalRecord:
    """
    Class untuk merepresentasikan rekam medis pasien.
    MedicalRecord tidak dapat berdiri sendiri tanpa Patient.
    """

    def __init__(
        self,
        record_id: int,
        patient: Patient,
        diagnosis: str,
        treatment: str,
    ):
        self.__record_id = record_id
        self.__patient = patient
        self.__diagnosis = diagnosis
        self.__treatment = treatment
        self.__timestamp = datetime.now()

    # ===== Getter =====
    def get_record_id(self) -> int:
        """Mengembalikan ID rekam medis."""
        return self.__record_id

    def get_patient(self) -> Patient:
        """Mengembalikan pasien terkait."""
        return self.__patient

    def get_diagnosis(self) -> str:
        """Mengembalikan diagnosis pasien."""
        return self.__diagnosis

    def get_treatment(self) -> str:
        """Mengembalikan tindakan medis."""
        return self.__treatment

    def get_timestamp(self) -> datetime:
        """Mengembalikan waktu pencatatan rekam medis."""
        return self.__timestamp

    # ===== Setter =====
    def set_diagnosis(self, diagnosis: str) -> None:
        """Mengubah diagnosis pasien."""
        if not diagnosis:
            raise ValueError("Diagnosis tidak boleh kosong")
        self.__diagnosis = diagnosis

    def set_treatment(self, treatment: str) -> None:
        """Mengubah tindakan medis."""
        if not treatment:
            raise ValueError("Tindakan medis tidak boleh kosong")
        self.__treatment = treatment

    # ===== Update Method =====
    def update_record(self, diagnosis: str, treatment: str) -> None:
        """
        Memperbarui diagnosis dan tindakan medis pasien.
        """
        self.set_diagnosis(diagnosis)
        self.set_treatment(treatment)
        self.__timestamp = datetime.now()