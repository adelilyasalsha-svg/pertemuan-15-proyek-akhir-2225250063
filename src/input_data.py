
def baca_data(path):
    """Membaca data siswa dari file teks."""
    data = []

    with open(path, "r", encoding="utf-8") as file:
        for nomor, baris in enumerate(file, start=1):
            baris = baris.strip()

            if not baris:
                continue

            bagian = baris.split(",")

            if len(bagian) != 2:
                print(f"Baris {nomor} dilewati: format tidak valid.")
                continue

            nama = bagian[0].strip()

            try:
                nilai = float(bagian[1].strip())
            except ValueError:
                print(f"Baris {nomor} dilewati: nilai bukan angka.")
                continue

            if not nama:
                print(f"Baris {nomor} dilewati: nama kosong.")
                continue

            data.append({
                "nama": nama,
                "nilai": nilai
            })

    return data
