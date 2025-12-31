from .person import Person


class Patient(Person):
    """
    Class untuk merepresentasikan pasien/korban bencana.
    Turunan dari class Person.
    """

    def __init__(
        self,
        person_id: int,
        name: str,
        age: int,
        condition: str,
        severity_level: int,
    ):
        super().__init__(person_id, name, age)
        self.__condition = condition
        self.__severity_level = severity_level

    # ===== Getter =====
    def get_condition(self) -> str:
        """Mengembalikan kondisi kesehatan pasien."""
        return self.__condition

    def get_severity_level(self) -> int:
        """Mengembalikan tingkat keparahan pasien."""
        return self.__severity_level

    # ===== Setter =====
    def set_condition(self, condition: str) -> None:
        """Mengubah kondisi kesehatan pasien."""
        if not condition:
            raise ValueError("Kondisi tidak boleh kosong")
        self.__condition = condition

    def set_severity_level(self, severity_level: int) -> None:
        """Mengubah tingkat keparahan pasien."""
        if severity_level < 1 or severity_level > 5:
            raise ValueError("Severity level harus antara 1 sampai 5")
        self.__severity_level = severity_level

    # ===== Business-light Method =====
    def update_condition(self, condition: str, severity_level: int) -> None:
        """
        Memperbarui kondisi dan tingkat keparahan pasien.
        """
        self.set_condition(condition)
        self.set_severity_level(severity_level)

    # ===== Polymorphism (Override) =====
    def get_role(self) -> str:
        """Mengembalikan peran dari object ini."""
        return "Patient"