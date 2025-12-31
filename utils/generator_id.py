import uuid


def generate_id() -> str:
    """
    Menghasilkan ID unik berbasis UUID v4.

    Returns:
        str: ID unik dalam bentuk string.
    """
    return str(uuid.uuid4())
# Contoh penggunaan:
# unique_id = generate_id()
# print(unique_id)  # Output: Sebuah UUID v4 unik, misalnya "f47ac10b-58cc-4372-a567-0e02b2c3d479"