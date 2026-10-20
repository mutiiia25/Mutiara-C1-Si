#
tugas = float(input("Nilai tugas :"))
uts = float(input("Nilai UTS :"))
uas = float(input("Nilai UAS :"))
kehadiran = float(input("Kehadiran :"))

# Menghitung nilai akhir
nilai_akhir = (20 / 100 * tugas) + (30 / 100 * uts) + (50 / 100 * uas)
print ("Nilai Akhir :", nilai_akhir)

# Menentukan status mahasiswa
if nilai_akhir < 75 or kehadiran <80:
    print ("Status     :  BELUM LULUS")
elif nilai_akhir >= 85 and kehadiran >= 90 and nilai_akhir % 2 == 0:
    print ("Status     :  LULUS DENGAN PREDIKAT")
else:
    print ("Status     :  LULUS")