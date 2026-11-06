
# ==========================================
#       PROGRAM APLIKASI KASIR RESTORAN
# ==========================================

print("==========================================")
print("          SELAMAT DATANG DI DJO CORNER")
print("             APLIKASI KASIR")
print("==========================================")

# Inisialisasi variabel
total = 0
jumlah_pesanan = 0

# Memulai perulangan pemesanan
while True:

    print("\n============== MENU MAKANAN ==============")
    print("1. Nasi Goreng    : Rp25.000")
    print("2. Mie Ayam       : Rp15.000")
    print("3. Ayam Geprek    : Rp20.000")
    print("4. Sate Ayam      : Rp30.000")
    print("5. Bakso          : Rp18.000")
    print("0. Selesai Memilih")
    print("==========================================")

    # Memasukkan pilihan menu
    pilihan = int(input("Masukkan pilihan menu (0-5): "))

    # Memeriksa pilihan menu
    if pilihan == 0:
        print("\nAnda telah selesai memilih menu.")
        break

    elif pilihan == 1:
        nama = "Nasi Goreng"
        harga = 25000

    elif pilihan == 2:
        nama = "Mie Ayam"
        harga = 15000

    elif pilihan == 3:
        nama = "Ayam Geprek"
        harga = 20000

    elif pilihan == 4:
        nama = "Sate Ayam"
        harga = 30000

    elif pilihan == 5:
        nama = "Bakso"
        harga = 18000

    else:
        print("Maaf, pilihan menu tidak tersedia!")
        print("Silakan pilih menu kembali.")
        continue

    # Memasukkan jumlah pesanan
    print("\nMenu yang dipilih :", nama)
    print("Harga satuan      : Rp", format(harga, ",").replace(",", "."))

    jumlah = int(input("Masukkan jumlah pesanan: "))

    # Memeriksa jumlah pesanan
    if jumlah <= 0:
        print("Jumlah pesanan tidak valid!")
        print("Silakan masukkan jumlah lebih dari 0.")
        continue

    # Menghitung subtotal
    subtotal = harga * jumlah

    # Menambahkan subtotal ke total belanja
    total = total + subtotal

    # Menghitung jumlah seluruh pesanan
    jumlah_pesanan = jumlah_pesanan + jumlah

    # Menampilkan rincian pesanan
    print("\n========== RINCIAN PESANAN ===========")
    print("Nama Makanan  :", nama)
    print("Harga         : Rp", format(harga, ",").replace(",", "."))
    print("Jumlah        :", jumlah)
    print("Subtotal      : Rp", format(subtotal, ",").replace(",", "."))
    print("-------------------------------------")
    print("Total Sementara: Rp", format(total, ",").replace(",", "."))
    print("=====================================")

# ==========================================
#             PROSES PEMBAYARAN
# ==========================================

print("\n==========================================")
print("              STRUK PEMBAYARAN")
print("==========================================")

print("Jumlah Pesanan : ", jumlah_pesanan)
print("Total Belanja  : Rp", format(total, ",").replace(",", "."))

# Memeriksa apakah mendapatkan diskon
if total > 200000:
    diskon = 20
    potongan = total * diskon // 100

    print("Selamat! Anda mendapatkan diskon 20%.")

else:
    diskon = 0
    potongan = 0

    print("Maaf, Anda tidak mendapatkan diskon.")

# Menghitung total pembayaran
total_bayar = total - potongan

# ==========================================
#             CETAK STRUK AKHIR
# ==========================================

print("\n============== STRUK AKHIR ===============")
print("Jumlah Pesanan : ", jumlah_pesanan)
print("Total Belanja  : Rp", format(total, ",").replace(",", "."))
print("Diskon         : ", diskon, "%")
print("Potongan       : Rp", format(potongan, ",").replace(",", "."))
print("------------------------------------------")
print("TOTAL BAYAR    : Rp", format(total_bayar, ",").replace(",", "."))
print("==========================================")
print("          TERIMA KASIH!")
print("       SELAMAT MENIKMATI MAKANAN")
print("==========================================")