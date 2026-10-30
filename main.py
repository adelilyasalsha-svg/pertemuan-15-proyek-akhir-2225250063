
from pathlib import Path

from src.input_data import baca_data
from src.proses import proses_data, hitung_statistik
from src.output import buat_laporan, tampilkan_laporan, simpan_laporan


BASE_DIR = Path(__file__).resolve().parent
FILE_DATA = BASE_DIR / "data" / "contoh_data.txt"
FILE_OUTPUT = BASE_DIR / "output" / "laporan.txt"


def main():
    try:
        data = baca_data(FILE_DATA)
    except OSError as error:
        print(f"Gagal membaca file data: {error}")
        return

    data_valid = proses_data(data)

    if not data_valid:
        print("Tidak ada data valid untuk dianalisis.")
        return

    statistik = hitung_statistik(data_valid)
    laporan = buat_laporan(data_valid, statistik)

    tampilkan_laporan(laporan)

    try:
        simpan_laporan(laporan, FILE_OUTPUT)
        print(f"\nLaporan tersimpan di: {FILE_OUTPUT}")
    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")


if __name__ == "__main__":
    main()
