# Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Deskripsi Proyek
Program ini dibuat menggunakan Python untuk merekap dan menganalisis nilai matematika siswa. Program membaca data dari file teks, memvalidasi nilai, menghitung statistik, menentukan status ketuntasan, dan menyimpan laporan hasil analisis.

## 2. Fitur Program
- Membaca data nilai siswa dari file teks.
- Memvalidasi nilai antara 0 sampai 100.
- Menghitung jumlah siswa.
- Menghitung rata-rata, nilai minimum, dan nilai maksimum.
- Menentukan status ketuntasan berdasarkan KKM 75.
- Menampilkan dan menyimpan laporan analisis.

## 3. Persyaratan
- Python 3.x
- Visual Studio Code (disarankan)

## 4. Cara Menjalankan
1. Buka folder proyek di Visual Studio Code.
2. Buka terminal pada folder utama proyek.
3. Jalankan perintah berikut:

```bash
python main.py
```

## 5. Struktur Folder
- `main.py`: menjalankan program utama.
- `src/__init__.py`: penanda paket Python.
- `src/input_data.py`: membaca data siswa.
- `src/proses.py`: memvalidasi dan menganalisis nilai.
- `src/output.py`: menyusun, menampilkan, dan menyimpan laporan.
- `data/contoh_data.txt`: menyimpan data contoh siswa.
- `tests/test_case.md`: dokumentasi skenario pengujian.
- `docs/screenshot/`: tempat menyimpan tangkapan layar pengujian.
- `output/`: tempat menyimpan laporan yang dihasilkan.

## 6. Data Contoh
| Nama | Nilai |
|---|---:|
| Ayu | 85 |
| Budi | 78 |
| Citra | 90 |
| Deni | 65 |
| Eka | 100 |

## 7. Hasil yang Diharapkan
- Jumlah siswa: 5
- Rata-rata: 83.60
- Nilai minimum: 65
- Nilai maksimum: 100
- Siswa tuntas: 4
- Siswa belum tuntas: 1

## 8. Pengujian
Skenario pengujian mencakup data normal, nilai batas bawah, nilai batas atas, nilai tidak valid, input bukan angka, data kosong, dan file tidak ditemukan.

Hasil aktual dan status pengujian dicatat dalam `tests/test_case.md` setelah pengujian dilakukan.

## 9. Known Issues
Masalah yang ditemukan selama pengujian akan dicatat dan diperbaiki. Masalah yang belum terselesaikan akan dituliskan berdasarkan hasil pengujian aktual.

## 10. Referensi dan Bantuan
- Bahan Ajar Pertemuan 14 dan Pertemuan 15.
- ChatGPT digunakan sebagai bantuan dalam penyusunan dan peninjauan kode.
