# utils/enums/enum_parser.py
from enum import Enum
from typing import Type, TypeVar

E = TypeVar("E", bound=Enum)


def parse_enum(enum_cls: Type[E], value: str) -> E:
    """
    Mengonversi input string menjadi Enum yang valid.

    Normalisasi dilakukan dengan lower() agar input user fleksibel.
    Contoh:
        "Aktif", "AKTIF", "aktif" -> StatusBencana.AKTIF

    Args:
        enum_cls (Type[Enum]): Kelas Enum tujuan.
        value (str): Nilai input (biasanya dari user).

    Returns:
        Enum: Anggota Enum yang sesuai.

    Raises:
        ValueError: Jika value tidak valid atau bukan string.
    """
    if not isinstance(value, str):
        raise ValueError("Nilai enum harus berupa string")

    try:
        return enum_cls(value.lower())
    except ValueError:
        valid_values = [e.value for e in enum_cls]
        raise ValueError(
            f"Nilai tidak valid. Pilihan yang tersedia: {valid_values}"
        )
# Contoh penggunaan:
# from utils.enums.status_bencana import StatusBencana
# status = parse_enum(StatusBencana, "Aktif")
# print(status)  # Output: StatusBencana.AKTIF