# Disaster Healthcare Management System 🚑
### Sistem Informasi Manajemen Penanganan Kesehatan Bencana

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Completed-success)

## 📖 Deskripsi Proyek
Aplikasi ini adalah sistem berbasis **Command Line Interface (CLI)** yang dirancang untuk membantu manajemen penanganan kesehatan dalam situasi bencana alam. Sistem ini mengelola data bencana, posko bantuan, tenaga medis, korban (pasien), stok obat-obatan, pemeriksaan medis (triage), hingga pembuatan resep obat secara terintegrasi.

Proyek ini dikembangkan sebagai **Ujian Akhir Semester (UAS) Praktikum Pemrograman Berorientasi Objek (PBO)** di Universitas Muhammadiyah Kalimantan Timur.

## 👥 Anggota Kelompok
**Kelompok: [MASUKKAN NAMA/NOMOR KELOMPOK ANDA]**

| No | Nama Mahasiswa | NIM |
|----|---------------|-----|
| 1. | Hafidzal Mufty | 2411102441285 |
| 2. | Haidar Halim | 2411102441309 |
| 3. | Hifzi Khairi | 2411102441227 |
| 4. | Muhammad Iqbal Nur Salim | 2411102441302 |
| 5. | Muhammad Nabiel | 241102441211 |
| 6. | Rivoldy Makatita | 2411102441207 |
| 7. | Rohmi Ihsan | 2411102441244 |

---

## 🏗️ Arsitektur Sistem (Layered Architecture)
Aplikasi ini dibangun menggunakan **Layered Architecture** untuk memisahkan tanggung jawab (*Separation of Concerns*) sesuai prinsip SOLID.

```text
.
├── models/          # Entitas/Data Class (Menyimpan struktur data seperti Obat, Korban, dll)
├── repositories/    # Data Access Layer (Menyimpan data in-memory/simulasi database)
├── services/        # Business Logic Layer (Validasi & alur proses bisnis)
├── utils/           # Fungsi bantuan (Logger, Enum, Generator ID)
└── main.py          # Entry Point & Orchestrator (Titik masuk aplikasi)