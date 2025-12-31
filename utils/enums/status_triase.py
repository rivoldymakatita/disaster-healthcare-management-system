from enum import Enum

class StatusTriase(Enum):
    MERAH = "Merah"      # Prioritas tinggi
    KUNING = "Kuning"    # Prioritas sedang
    HIJAU = "Hijau"      # Prioritas rendah
    HITAM = "Hitam"      # Tidak dapat diselamatkan