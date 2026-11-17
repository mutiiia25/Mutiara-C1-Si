print("===================================")
print("     APLIKASI TIKET BIOSKOP")
print("===================================")

while True:
# 1. Input nama pelanggan
    nama = input("\nMasukkan nama pelanggan: ")

# 2. Input jenis tiket
    print("\nPilihan Jenis Tiket:")
    print("1. Reguler  - Rp35.000")
    print("2. VIP      - Rp50.000")
    print("3. Premium  - Rp75.000")

    jenis = input("Pilih jenis tiket (1/2/3): ")
    jumlah = int(input("Masukkan jumlah tiket: "))

# 3. Menentukan harga tiket
    if jenis == "1":
        nama_tiket = "Reguler"
        harga = 35000
    elif jenis == "2":
        nama_tiket = "VIP"
        harga = 50000
    elif jenis == "3":
        nama_tiket = "Premium"
        harga = 75000
    else:
        print("Pilihan tiket tidak tersedia!")
        continue

# 4. Menghitung total harga
    total = harga * jumlah

# 5. Mengecek diskon
    if jumlah > 3:
        diskon = total * 10 / 100
    else:
        diskon = 0

    pembayaran = total - diskon

# 6. Menampilkan hasil pemesanan
    print("\n===================================")
    print("       STRUK PEMESANAN TIKET")
    print("=====================================")
    print("Nama Pelanggan :", nama)
    print("Jenis Tiket    :", nama_tiket)
    print("Jumlah Tiket   :", jumlah)
    print("Harga Tiket    : Rp", format(harga, ","))
    print("Total Harga    : Rp", format(total, ","))
    print("Diskon         : Rp", format(diskon, ","))
    print("-----------------------------------")
    print("Total Bayar    : Rp", format(pembayaran, ","))
    print("===================================")

# 7. Melayani pelanggan berikutnya
    ulang = input("\nApakah ingin melayani pelanggan berikutnya? (ya/tidak): ")

    if ulang.lower() != "ya":
        print("\nTerima kasih telah memesan tiket!")
        print("Program selesai.")
        break