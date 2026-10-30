
KKM = 75


def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada pada rentang 0 sampai 100."""
    return 0 <= nilai <= 100


def proses_data(data, kkm=KKM):
    """Memvalidasi nilai dan menentukan status ketuntasan."""
    hasil = []

    for siswa in data:
        nama = siswa["nama"]
        nilai = siswa["nilai"]

        if not validasi_nilai(nilai):
            print(
                f"Nilai {nama} ditolak: "
                "nilai harus antara 0 dan 100."
            )
            continue

        status = "Tuntas" if nilai >= kkm else "Belum Tuntas"

        hasil.append({
            "nama": nama,
            "nilai": nilai,
            "status": status
        })

    return hasil


def hitung_statistik(data):
    """Menghitung ringkasan statistik nilai siswa."""
    if not data:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "tuntas": 0,
            "belum_tuntas": 0
        }

    daftar_nilai = [siswa["nilai"] for siswa in data]

    return {
        "jumlah": len(data),
        "rata_rata": sum(daftar_nilai) / len(daftar_nilai),
        "minimum": min(daftar_nilai),
        "maksimum": max(daftar_nilai),
        "tuntas": sum(
            siswa["status"] == "Tuntas" for siswa in data
        ),
        "belum_tuntas": sum(
            siswa["status"] == "Belum Tuntas" for siswa in data
        )
    }
