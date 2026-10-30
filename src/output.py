
from pathlib import Path


def buat_laporan(data, statistik):
    """Menyusun laporan hasil analisis nilai siswa."""
    baris = [
        "LAPORAN REKAP DAN ANALISIS NILAI MATEMATIKA KELAS",
        "=" * 50,
        f"KKM: 75",
        f"Jumlah siswa: {statistik['jumlah']}",
        f"Rata-rata: {statistik['rata_rata']:.2f}",
        f"Nilai minimum: {statistik['minimum']}",
        f"Nilai maksimum: {statistik['maksimum']}",
        f"Siswa tuntas: {statistik['tuntas']}",
        f"Siswa belum tuntas: {statistik['belum_tuntas']}",
        "",
        "DAFTAR NILAI SISWA",
        "-" * 50
    ]

    for siswa in data:
        baris.append(
            f"{siswa['nama']}: {siswa['nilai']:g} "
            f"- {siswa['status']}"
        )

    return "\n".join(baris)


def tampilkan_laporan(laporan):
    """Menampilkan laporan pada terminal."""
    print(laporan)


def simpan_laporan(laporan, path):
    """Menyimpan laporan ke file teks."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(laporan + "\n", encoding="utf-8")
