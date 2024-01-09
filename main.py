# Definisikan daftar opsi pilihan makanan/minuman dan harga
menu = {
    "Sate": 20000,
    "Bakso": 15000,
    "Mie Ayam": 10000,
    "Es Teh": 5000,
    "Air Mineral": 4000,
}

# Inisialisasi list pesanan di luar loop while
pesanan = []

# Mulai transaksi
print("Selamat datang di Rumah Makan Tiga Berlian!")

# Permintaan input pilihan makanan dari pengguna
while True:
    print("Pilih menu makanan/minuman yang ingin Anda pesan:")
    for key, value in menu.items():
        print(f"{key}: Rp{value}")

    pilihan = input("Masukkan pilihan Anda (tekan x untuk selesai): ")

    # Jika pilihan pengguna adalah x, maka hentikan transaksi
    if pilihan == "x":
        break

    # Jika pilihan pengguna tidak valid, maka minta input ulang
    if pilihan not in menu:
        print("Pilihan Anda tidak valid. Silahkan pilih kembali.")
        continue

    # Menambahkan menu yang dipilih ke dalam list pesanan
    pesanan.append(pilihan)

# Hitung total harga pesanan
total_harga = sum(menu[menu_item] for menu_item in pesanan)

# Tampilkan struk pembelian
print("--------------------------------------------------")
print("Struk Pembelian Menu Rumah Makan Tiga Berlian")
print("--------------------------------------------------")
print("No. | Menu | Harga")
print("----|------|------")
for i, menu_item in enumerate(pesanan):
    print(f"{i + 1} | {menu_item} | Rp{menu[menu_item]}")
print("--------------------------------------------------")
print(f"Total Harga: Rp{total_harga}")
print("--------------------------------------------------")