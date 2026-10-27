# variabel dan tipe data
nama_mhs = "Mutiara"
kelas = "C1"

nalgoritma = 90
nagama = 90
nbasisdata = 90

# rata_rata = (nalgoritma + nagama + nbasisdata) / 3
# print(rata_rata)
nilai = int(input("Masukkan Nilai :"))

# penentuan lulus atau tidak
if nilai >=80 and nilai <=100:
    # kondisi jika terpenuhi
    # maka
    print("Nilai : A")
elif nilai >=70 and nilai <=80:
    print("Nilai : B")
elif nilai >=50 and nilai <=70:
    print("Nilai : C")
else:
    # cukup menampilkan hasil
    # maka
    print("Nilai lebih dari 100 atau dibawah 50")