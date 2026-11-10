## Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai
if nama == "Andi":
    target = 70
elif nama == "Budi":
    target = 75
elif nama == "Citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    target = 0

# Proses ujian
if target != 0:
    print("Nama Mahasiswa :", nama)
    print("Target Nilai   :", target)

    percobaan = 1
    lulus = False

    while percobaan <= 3:
        print("\nPercobaan ke-", percobaan)

        nilai = int(input("Masukkan nilai ujian: "))

        if nilai >= target:
            lulus = True
        else:
            print("Nilai belum mencapai target.")

            if percobaan < 3:
                print("Silakan mengikuti remedial.")
            else:
                print("Kesempatan remedial telah habis.")

        percobaan += 1

    # Hasil akhir
    print("\n=================================")
    print("          HASIL UJIAN")
    print("===================================")

    if lulus:
        print(nama, "berhasil LULUS!")
        print("setelah 3 kali percobaan")
    else:
        print(nama, "dinyatakan TIDAK LULUS!")
        print("telah melakukan 3 kali percobaan.")

    print("===================================")