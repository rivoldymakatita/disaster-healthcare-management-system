from datetime import datetime


class DateHelper:
    """
    Helper untuk mengelola dan memformat tanggal dan waktu.
    """

    @staticmethod
    def sekarang():
        """
        Mengembalikan timestamp saat ini (datetime object).
        """
        return datetime.now()

    @staticmethod
    def format_timestamp(timestamp, format_output="%d-%m-%Y %H:%M:%S"):
        """
        Mengubah timestamp menjadi string sesuai format.

        Default format:
        DD-MM-YYYY HH:MM:SS
        """
        if not isinstance(timestamp, datetime):
            raise ValueError("Timestamp harus bertipe datetime")

        return timestamp.strftime(format_output)
