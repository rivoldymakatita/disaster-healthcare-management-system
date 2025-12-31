from services.patient_service import PatientService
from services.medical_service import MedicalService
from repositories.patient_repository import PatientRepository
from repositories.medical_record_repository import MedicalRecordRepository
from utils.logger import setup_logger

logger = setup_logger()


def tampilkan_menu():
    print("\n=== Sistem Penanganan Kesehatan Bencana ===")
    print("1. Tambah Pasien")
    print("2. Lihat Pasien")
    print("3. Proses Penanganan")
    print("4. Keluar")


def tambah_pasien(service_pasien):
    try:
        nama = input("Nama Pasien: ").strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong")

        umur = int(input("Umur: "))

        service_pasien.register_patient(nama, umur)
        logger.info("Pasien berhasil ditambahkan")

    except ValueError as e:
        logger.warning(f"Input tidak valid: {e}")
    except Exception:
        logger.error("Gagal menambahkan pasien", exc_info=True)


def tampilkan_pasien(service_pasien):
    try:
        daftar_pasien = service_pasien.get_all_patients()
        if not daftar_pasien:
            logger.info("Belum ada data pasien")
            return

        for pasien in daftar_pasien:
            print(str(pasien))

    except Exception:
        logger.error("Gagal menampilkan data pasien", exc_info=True)


def proses_penanganan(service_medis):
    try:
        id_pasien = input("ID Pasien: ").strip()
        if not id_pasien:
            raise ValueError("ID pasien tidak boleh kosong")

        diagnosis = input("Diagnosis: ").strip()
        tindakan = input("Tindakan Medis: ").strip()

        service_medis.process_medical_record(
            id_pasien, diagnosis, tindakan
        )
        logger.info("Proses penanganan pasien berhasil")

    except ValueError as e:
        logger.warning(f"Input tidak valid: {e}")
    except Exception:
        logger.error("Proses penanganan pasien gagal", exc_info=True)


def main():
    repository_pasien = PatientRepository()
    repository_rekam_medis = MedicalRecordRepository()

    service_pasien = PatientService(repository_pasien)
    service_medis = MedicalService(
        repository_rekam_medis, repository_pasien
    )

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            tambah_pasien(service_pasien)
        elif pilihan == "2":
            tampilkan_pasien(service_pasien)
        elif pilihan == "3":
            proses_penanganan(service_medis)
        elif pilihan == "4":
            logger.info("Aplikasi dihentikan oleh pengguna")
            break
        else:
            logger.warning("Pilihan menu tidak valid")


if __name__ == "__main__":
    main()
