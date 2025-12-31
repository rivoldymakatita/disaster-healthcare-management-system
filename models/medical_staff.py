from .person import Person
from .patient import Patient


class MedicalStaff(Person):
    """
    Class untuk merepresentasikan tenaga medis
    dalam sistem penanganan kesehatan bencana.
    """

    def __init__(
        self,
        person_id: int,
        name: str,
        age: int,
        role: str,
        license_number: str,
    ):
        super().__init__(person_id, name, age)
        self.__role = role
        self.__license_number = license_number

    # ===== Getter =====
    def get_staff_role(self) -> str:
        """Mengembalikan peran tenaga medis."""
        return self.__role

    def get_license_number(self) -> str:
        """Mengembalikan nomor lisensi tenaga medis."""
        return self.__license_number

    # ===== Setter =====
    def set_staff_role(self, role: str) -> None:
        """Mengubah peran tenaga medis."""
        if not role:
            raise ValueError("Peran tenaga medis tidak boleh kosong")
        self.__role = role

    def set_license_number(self, license_number: str) -> None:
        """Mengubah nomor lisensi tenaga medis."""
        if not license_number:
            raise ValueError("Nomor lisensi tidak boleh kosong")
        self.__license_number = license_number

    # ===== Domain Method =====
    def treat_patient(self, patient: Patient) -> str:
        """
        Menangani pasien.
        (Logika detail akan diatur oleh service layer)
        """
        return f"Medical staff {self.get_name()} menangani pasien {patient.get_name()}"

    # ===== Polymorphism (Override) =====
    def get_role(self) -> str:
        """Mengembalikan peran dari object ini."""
        return "Medical Staff"