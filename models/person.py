from abc import ABC, abstractmethod


class Person(ABC):
    """
    Abstract base class untuk merepresentasikan manusia
    dalam sistem penanganan kesehatan bencana.
    """

    def __init__(self, person_id: int, name: str, age: int):
        self.__id = person_id
        self.__name = name
        self.__age = age

    # ===== Getter =====
    def get_id(self) -> int:
        """Mengembalikan ID person."""
        return self.__id

    def get_name(self) -> str:
        """Mengembalikan nama person."""
        return self.__name

    def get_age(self) -> int:
        """Mengembalikan umur person."""
        return self.__age

    # ===== Setter =====
    def set_name(self, name: str) -> None:
        """Mengubah nama person."""
        if not name:
            raise ValueError("Nama tidak boleh kosong")
        self.__name = name

    def set_age(self, age: int) -> None:
        """Mengubah umur person."""
        if age <= 0:
            raise ValueError("Umur harus lebih dari 0")
        self.__age = age

    # ===== Abstract Method (Polymorphism) =====
    @abstractmethod
    def get_role(self) -> str:
        """
        Method abstrak untuk mengembalikan peran person.
        Harus dioverride oleh child class.
        """
        pass