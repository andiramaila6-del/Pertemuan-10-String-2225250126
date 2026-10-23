def normalisasi_nama(nama):
    nama = nama.strip()
    nama = " ".join(nama.split())
    nama = nama.title()
    return nama


def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial


def normalisasi_kode(kode):
    kode = kode.strip()
    kode = " ".join(kode.split())
    kode = kode.replace(" ", "-")
    kode = kode.upper()
    return kode


nama = input("Nama: ")
kode = input("Kode kelas: ")

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
inisial = buat_inisial(nama_bersih)
jumlah_kata = len(nama_bersih.split())

print("\nNama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)