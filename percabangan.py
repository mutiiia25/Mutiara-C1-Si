
# variabel dan tipe data
nama_mhs = input("Masukkan Nama Mahasiswa: ")

# input nilai mata kuliah
algoritma = int(input("Masukkan Nilai Algoritma: "))
basisdata = int(input("Masukkan Nilai Basis Data: "))
pengantarteknologi = int(input("Masukkan Nilai Pengantar Teknologi: "))
inggris = int(input("Masukkan Nilai Bahasa Inggris: "))
pancasila = int(input("Masukkan Nilai Pancasila: "))
agama = int(input("Masukkan Nilai Agama: "))
logikainformatika = int(input("Masukkan Nilai Logika Informatika: "))

# menghitung rata-rata
rata_rata = (algoritma + basisdata + pengantarteknologi + inggris + pancasila + agama +logikainformatika) / 7

# menampilkan data mahasiswa
print("Nama Mahasiswa:", nama_mhs)

# penentuan nilai huruf
if rata_rata >= 80 and rata_rata <= 100:
    print("Nilai: A")
elif rata_rata >= 70 and rata_rata < 80:
    print("Nilai: B")
elif rata_rata >= 60 and rata_rata < 70:
    print("Nilai: C")
elif rata_rata >= 50 and rata_rata < 60:
    print("Nilai: D")
elif rata_rata >= 0 and rata_rata < 50:
    print("Nilai: E")
else:
    print("Nilai tidak valid")