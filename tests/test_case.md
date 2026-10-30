# Test Case Program Rekap dan Analisis Nilai Matematika Kelas

**KKM:** 75

| ID | Skenario | Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| TC01 | Data normal | Nilai 85, 78, 90, 65, 100 | Jumlah 5 siswa, rata-rata 83.60, minimum 65, maksimum 100, 4 tuntas, 1 belum tuntas | Jumlah 5 siswa, rata-rata 83.60, minimum 65, maksimum 100, 4 tuntas, 1 belum tuntas | PASS |
| TC02 | Nilai batas bawah | Nilai 0 | Nilai diterima dan status Belum Tuntas | Nilai diterima dan status Belum Tuntas | PASS |
| TC03 | Nilai batas atas | Nilai 100 | Nilai diterima dan status Tuntas | Nilai diterima dan status Tuntas | PASS* |
| TC04 | Nilai melebihi batas | Nilai 101 | Nilai ditolak karena melebihi 100 | Nilai ditolak karena melebihi 100 | PASS |
| TC05 | Nilai negatif | Nilai -1 | Nilai ditolak karena kurang dari 0 | Nilai ditolak karena kurang dari 0 | PASS |
| TC06 | Input bukan angka | Nilai `abc` | Baris dilewati karena nilai bukan angka | Baris dilewati karena nilai bukan angka | PASS |
| TC07 | Data kosong | File data kosong | Program menampilkan pesan tidak ada data valid untuk dianalisis | Program menampilkan pesan tidak ada data valid untuk dianalisis | PASS |
| TC08 | File tidak ditemukan | File `data/contoh_data.txt` tidak tersedia | Program menampilkan pesan gagal membaca file data | Program menampilkan pesan gagal membaca file data | PASS |

## Kesimpulan

Pengujian dirancang untuk memeriksa pengolahan data normal, batas nilai, input yang tidak valid, data kosong, dan penanganan file yang tidak ditemukan. Program dinyatakan berhasil apabila hasil aktual sesuai dengan hasil yang diharapkan pada setiap skenario.