# **Deskripsi Sistem (System Description)**

**Judul:** _Sistem Penanganan Kesehatan Bencana – CLI Application_

**Deskripsi Singkat:**
Aplikasi CLI ini dirancang untuk membantu proses penanganan kesehatan pada situasi bencana di Indonesia. Sistem berfungsi untuk mendata korban, mencatat kondisi kesehatan, mengelola tenaga medis, mendistribusikan obat/logistik kesehatan, dan membuat laporan situasional yang dapat digunakan tim penanggulangan bencana.

**Tujuan Sistem:**

1. Mengelola data korban secara cepat dan terstruktur.
2. Menyediakan informasi kondisi korban untuk prioritas penanganan (triage).
3. Mendukung pengelolaan tenaga medis (dokter, perawat).
4. Mencatat kebutuhan dan distribusi logistik kesehatan.
5. Menyediakan laporan kondisi kesehatan lapangan.
6. Memudahkan tim lapangan mengambil keputusan secara cepat melalui CLI.

**Pengguna Sistem (Actors):**

- **Petugas Medis (User)**
- **Administrator Medis (Admin)**

---

# **Alur Bisnis Global (Business Flow Overview)**

Berikut alur kerja utama dari aplikasi:

1. **Login User/Admin**
   Sistem membedakan hak akses (admin punya akses kelola tenaga medis & logistik).

2. **Pendataan Korban**

   - Input identitas korban
   - Input kondisi & tingkat keparahan (triage: Hijau, Kuning, Merah)

3. **Pendataan Tenaga Medis** (Admin)

   - Tambah/edit dokter & perawat
   - Cek ketersediaan

4. **Manajemen Logistik Kesehatan**

   - Tambah stok obat
   - Distribusi obat untuk korban
   - Cek ketersediaan

5. **Penanganan Korban**

   - Tugas tenaga medis
   - Pencatatan perawatan
   - Update kondisi korban

6. **Pembuatan Laporan**

   - Laporan jumlah korban berdasarkan status
   - Laporan tenaga medis tersedia
   - Laporan penggunaan logistik

Semua dilakukan melalui menu CLI dan diproses menggunakan OOP + Layered Architecture.

---

- **OOP secara penuh** (Encapsulation, Inheritance, Polymorphism)
- **Layered Architecture (3 Layer)**

  1. **UI Layer** – menu CLI & input user
  2. **Service Layer** – logika bisnis
  3. **Repository Layer** – penyimpanan data in-memory

---

## **Arsitektur Layered**

### **A. UI Layer**

- `MenuController`
- Menangani input/output pengguna
- Tidak menyimpan logika bisnis

### **B. Service Layer**

Mengolah data dengan aturan bisnis:

- `VictimService`
- `MedicalStaffService`
- `LogisticsService`

Contoh logika:

- Menentukan prioritas korban berdasarkan triage
- Mengalokasikan tenaga medis yang tersedia
- Mengurangi stok obat saat distribusi

### **C. Repository Layer**

Menyimpan data sementara (in-memory):

- `VictimRepository`
- `MedicalStaffRepository`
- `MedicineRepository`

Menggunakan struktur data seperti array/list.

---

## **Konsep OOP yang digunakan**

### **1. Encapsulation**

Semua atribut bersifat **private**. Akses melalui method publik.

### **2. Inheritance**

- Doctor & Nurse mewarisi MedicalStaff

### **3. Polymorphism**

- Method `displayInfo()` pada MedicalStaff di-_override_ oleh Doctor & Nurse
- Method `assignTask()` dapat memiliki implementasi berbeda

### **4. Abstraction**

- MedicalStaff dibuat abstract class untuk menyederhanakan perilaku bersama