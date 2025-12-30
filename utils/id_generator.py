import uuid

def generate_id():
    """
    Generate ID unik untuk entitas (pasien, rekam medis, dll)
    """
    return str(uuid.uuid4())
