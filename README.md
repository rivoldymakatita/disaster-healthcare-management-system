# Disaster Response System (CLI)

UAS Praktikum Pemrograman Berorientasi Objek (Python)

## Deskripsi Proyek
  
Aplikasi Disaster Response System merupakan aplikasi berbasis Command Line Interface (CLI) yang dikembangkan untuk membantu penanganan bencana alam di Indonesia.
Sistem ini dibangun menggunakan konsep Object-Oriented Programming (OOP) secara menyeluruh serta menerapkan Layered Architecture untuk memisahkan data, logika bisnis, dan antarmuka aplikasi.
Proyek ini dibuat untuk memenuhi Ujian Akhir Semester (UAS) Praktikum Pemrograman Berorientasi Objek.

## Tema Studi Kasus

Sistem Penanganan Kesehatan Bencana
Sistem ini berfokus pada pengelolaan data pasien, tenaga medis, dan pencatatan laporan kesehatan selama kondisi darurat bencana.

## Struktur Proyek

Struktur folder proyek mengikuti ketentuan Modul 6 & 13 :
UAS-disaster-healthcare-management-system/
│
├── models/ # Definisi class & entitas (Data Layer)
├── repositories/ # Penyimpanan data (List/Dict simulation)
├── services/ # Logika bisnis & interface (SOLID)
├── utils/ # Fungsi bantuan (format waktu, dll)
├── main.py # Entry point / orchestrator aplikasi
└── README.md # Dokumentasi proyek

## Konsep OOP yang Diterapkan

Proyek ini menerapkan konsep OOP berikut:
Class & Object
Setiap entitas seperti Pasien dan Tenaga Medis direpresentasikan dalam bentuk class.

Enkapsulasi
Atribut penting menggunakan akses private (\_\_ (2 garis bawah)) dan dikelola melalui getter dan setter dengan validasi.

Inheritance
Digunakan untuk menghindari duplikasi kode antar class yang memiliki hubungan is-a.

Polimorfisme
Menerapkan method overriding untuk menyesuaikan perilaku method pada child class.

## Prinsip SOLID

Beberapa prinsip SOLID yang diterapkan dalam sistem ini:

SRP (Single Responsibility Principle)
Setiap class hanya memiliki satu tanggung jawab.

DIP (Dependency Inversion Principle)
Service bergantung pada abstraksi (ABC), bukan implementasi konkret repository.

OCP (Open/Closed Principle)
Sistem dapat dikembangkan tanpa mengubah kode yang sudah ada.

## Fitur Teknis

Penerapan logging (INFO, WARNING, ERROR) sebagai pengganti print()
Penggunaan library standar datetime untuk pencatatan waktu
Validasi data untuk mencegah error dan crash
Docstring pada setiap class dan method (Google Style)

## Cara Menjalankan Program

Pastikan Python sudah terinstal, lalu jalankan perintah berikut:

python main.py

## Dokumentasi & Desain

UML Class Diagram dibuat sebelum proses coding
Kode telah melalui tahap refactoring
Struktur proyek sesuai dengan ketenuan soal UAS
Proyek dikelola menggunakan Git

## Anggota Kelompok

HAFIDZAL MUFTY - 2411102441285
HAIDAR HALIM - 2411102441309
HIFZI KHAIRI - 2411102441227
MUHAMMAD IQBAL NUR SALIM -2411102441302
MUHAMMAD NABIEL - 241102441211
RIVOLDY MAKATITA - 2411102441207
ROHMI IHSAN - 2411102441244
