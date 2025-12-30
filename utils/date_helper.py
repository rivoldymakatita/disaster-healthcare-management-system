from datetime import datetime

def get_current_date():
    """
    Mengembalikan tanggal saat ini (YYYY-MM-DD)
    """
    return datetime.now().strftime("%Y-%m-%d")

def get_current_time():
    """
    Mengembalikan waktu saat ini (HH:MM:SS)
    """
    return datetime.now().strftime("%H:%M:%S")
