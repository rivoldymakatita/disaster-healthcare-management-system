from datetime import date

# Import Repositories
from repositories.bencana_repository import BencanaRepositoryMemory
from repositories.posko_repository import PoskoRepositoryMemory
from repositories.orang_repository import OrangRepositoryMemory
from repositories.tenaga_medis_repository import TenagaMedisRepositoryMemory
from repositories.korban_repository import KorbanRepositoryMemory
from repositories.obat_repository import ObatRepositoryMemory
from repositories.pemeriksaan_repository import PemeriksaanRepositoryMemory
from repositories.resep_obat_repository import ResepObatRepositoryMemory

# Import Services
from services.bencana_service import BencanaService
from services.posko_service import PoskoService
from services.tenaga_medis import TenagaMedisService
from services.korban_service import KorbanService
from services.obat_service import ObatService
from services.pemeriksaan_service import PemeriksaanService
from services.resep_obat_service import ResepObatService

def main():
    print("=== MENGINISIALISASI SISTEM MANAJEMEN KESEHATAN BENCANA ===\n")

    # 1. Inisialisasi Repository
    bencana_repo = BencanaRepositoryMemory()
    posko_repo = PoskoRepositoryMemory()
    orang_repo = OrangRepositoryMemory()
    tm_repo = TenagaMedisRepositoryMemory()
    korban_repo = KorbanRepositoryMemory()
    obat_repo = ObatRepositoryMemory()
    pemeriksaan_repo = PemeriksaanRepositoryMemory()
    resep_repo = ResepObatRepositoryMemory()

    # 2. Inisialisasi Service (Dependency Injection)
    bencana_service = BencanaService(bencana_repo)
    posko_service = PoskoService(posko_repo, bencana_repo)
    tm_service = TenagaMedisService(tm_repo, orang_repo, posko_repo)
    korban_service = KorbanService(korban_repo, orang_repo, posko_repo)
    obat_service = ObatService(obat_repo)
    pemeriksaan_service = PemeriksaanService(pemeriksaan_repo, korban_repo, tm_repo, orang_repo)
    resep_service = ResepObatService(resep_repo, pemeriksaan_repo, obat_repo)

    try:
        # 3. Skenario: Membuat Data Bencana
        print("[1] Membuat Bencana...")
        id_bencana = bencana_service.buat_bencana(
            jenis="Gempa Bumi",
            lokasi="Cianjur",
            tanggal_mulai=date.today(),
            status="aktif"
        )
        print(f"   -> Bencana berhasil dibuat. ID: {id_bencana}")

        # 4. Skenario: Membuat Posko
        print("\n[2] Membuat Posko...")
        id_posko = posko_service.buat_posko(
            bencana_id=id_bencana,
            nama_posko="Posko Utama Alun-alun",
            alamat_posko="Jl. Raya No. 1",
            kapasitas_posko=100,
            status_posko="aktif"
        )
        print(f"   -> Posko berhasil dibuat. ID: {id_posko}")

        # 5. Skenario: Mendaftarkan Tenaga Medis
        print("\n[3] Mendaftarkan Tenaga Medis...")
        id_dokter = tm_service.buat_tenaga_medis(
            nama_orang="Dr. Budi Santoso",
            alamat_orang="Jakarta",
            jenis_kelamin_orang="laki-laki",
            tanggal_lahir_orang=date(1985, 5, 20),
            id_posko=id_posko,
            no_izin_praktik="SIP-12345",
            role="Dokter",
            spesialisasi="Umum"
        )
        print(f"   -> Dokter berhasil didaftarkan. ID: {id_dokter}")

        # 6. Skenario: Mendaftarkan Korban
        print("\n[4] Mendaftarkan Korban...")
        id_korban = korban_service.buat_korban(
            nama_orang="Ahmad",
            alamat_orang="Cianjur Desa A",
            jenis_kelamin_orang="laki-laki",
            tanggal_lahir_orang=date(1990, 1, 1),
            status_triase="Kuning",
            kondisi_awal="Luka ringan di kaki",
            lokasi_ditemukan="Reruntuhan Rumah",
            id_posko=id_posko
        )
        print(f"   -> Korban berhasil didaftarkan. ID: {id_korban}")

        # 7. Skenario: Menambahkan Stok Obat
        print("\n[5] Menambahkan Obat ke Inventory...")
        id_obat_paracetamol = obat_service.buat_obat(
            nama="Paracetamol 500mg",
            stok=100,
            satuan="Tablet",
            tanggal_kadaluarsa=date(2026, 12, 31)
        )
        id_obat_betadine = obat_service.buat_obat(
            nama="Betadine Cair",
            stok=50,
            satuan="Botol",
            tanggal_kadaluarsa=date(2026, 6, 30)
        )
        print(f"   -> Obat Paracetamol dibuat. ID: {id_obat_paracetamol}")
        print(f"   -> Obat Betadine dibuat. ID: {id_obat_betadine}")

        # 8. Skenario: Pemeriksaan Medis
        print("\n[6] Melakukan Pemeriksaan...")
        id_pemeriksaan = pemeriksaan_service.buat_pemeriksaan(
            id_korban=id_korban,
            id_tenaga_medis=id_dokter,
            keluhan="Nyeri pada kaki kanan",
            diagnosa="Luka lecet dan memar ringan",
            status_triase="Hijau", # Status membaik dari Kuning -> Hijau
            sinkron_triase_korban=True
        )
        print(f"   -> Pemeriksaan selesai. ID: {id_pemeriksaan}")
        
        # Cek apakah status triase korban berubah
        korban = korban_service.ambil_korban(id_korban)
        print(f"   -> Status Triase Korban sekarang: {korban.get_status_triase().value}")

        # 9. Skenario: Membuat Resep Obat
        print("\n[7] Membuat Resep Obat...")
        items_resep = [
            {
                "id_obat": id_obat_paracetamol,
                "qty": 10,
                "aturan_pakai": "3x1 sesudah makan",
                "dosis": 500
            },
            {
                "id_obat": id_obat_betadine,
                "qty": 1,
                "aturan_pakai": "Oleskan 2x sehari",
                "dosis": 1
            }
        ]
        
        id_resep = resep_service.buat_resep(
            id_pemeriksaan=id_pemeriksaan,
            items_input=items_resep
        )
        print(f"   -> Resep obat berhasil dibuat. ID: {id_resep}")

        # Cek pengurangan stok
        stok_paracetamol = obat_service.ambil_obat(id_obat_paracetamol).get_stock_obat()
        print(f"   -> Sisa stok Paracetamol: {stok_paracetamol} (Awal: 100, Keluar: 10)")

        print("\n=== SIMULASI SELESAI DENGAN SUKSES ===")

    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()