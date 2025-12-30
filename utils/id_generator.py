import uuid
from datetime import datetime


class IdGenerator:
    """
    Generator ID unik untuk entitas dalam sistem
    (pasien, rekam medis, dll).
    """

    @staticmethod
    def buat_id(prefix):
        """
        Membuat ID unik dengan format:
        PREFIX-YYYYMMDD-HHMMSS-UUID4

        Contoh:
        PASIEN-20251230-235959-a1b2c3d4
        """
        waktu = datetime.now().strftime("%Y%m%d-%H%M%S")
        unik = uuid.uuid4().hex[:8]
        return f"{prefix}-{waktu}-{unik}"
