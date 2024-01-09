## PROJECT UAS
| Variable | Isi |
| -------- | --- |
| Nama | RADITYA TANSY LIZARA  |
| NIM | 312310454 |
| Kelas | TI.23.A5 |
| Mata Kuliah | Bahasa Pemrograman |

### Link Youtube Penjelasan PROJECT UAS : https://youtu.be/eCffFEohLvE?si=_OBKvpLNTchPmlMT

### Buatlah program kasir di sebuah kantin, dengan kondisi berikut:
* List opsi pilihan makanan/minuman dan aksi, bisa menggunakan
format dictionary
* Program harus meminta input pilihan makanan dari pengguna.
* Program harus menghitung total harga makanan yang dipesan.
* Program harus menampilkan struk pembelian

### Definisi daftar opsi pilihan makanan/minuman dan harga
Bagian ini mendefinisikan sebuah dictionary bernama menu yang berisi daftar opsi pilihan makanan/minuman dan harga masing-masing.
```python
menu = {
    "Sate": 20000,
    "Bakso": 15000,
    "Mie Ayam": 10000,
    "Es Teh": 5000,
    "Air Mineral": 4000,
}
```
### Inisialisasi list pesanan di luar loop while
Bagian ini menginisialisasi sebuah list bernama pesanan yang akan digunakan untuk menyimpan daftar pesanan pelanggan.
```python
pesanan = []
```
### Mulai transaksi
Bagian ini menampilkan pesan selamat datang dan memulai transaksi pembelian.
```python
print("Selamat datang di Rumah Makan Tiga Berlian!")
```
### Permintaan input pilihan makanan dari pengguna
Bagian ini menampilkan daftar menu yang tersedia dan meminta input dari pengguna untuk memilih menu yang ingin dipesan.
```python
while True:
    print("Pilih menu makanan/minuman yang ingin Anda pesan:")
    for key, value in menu.items():
        print(f"{key}: Rp{value}")

    pilihan = input("Masukkan pilihan Anda (tekan x untuk selesai): ")
```
### Penanganan input pilihan pengguna
Bagian ini menangani input pilihan pengguna dengan cara berikut:

* Jika pilihan pengguna adalah "x", maka transaksi dihentikan.
```python
if pilihan == "x":
        break
```
* Jika pilihan pengguna tidak ada dalam dictionary `menu`, maka pengguna diminta untuk memasukkan input ulang.
```python
if pilihan not in menu:
        print("Pilihan Anda tidak valid. Silahkan pilih kembali.")
        continue
```
* Jika pilihan pengguna ada dalam dictionary `menu`, maka menu tersebut ditambahkan ke dalam list `pesanan`.
```python
pesanan.append(pilihan)
```
### Hitung total harga pesanan
Bagian ini menghitung total harga pesanan dengan cara menjumlahkan harga masing-masing menu yang dipesan.
```python
total_harga = sum(menu[menu_item] for menu_item in pesanan)
```
### Tampilkan struk pembelian
Bagian ini menampilkan struk pembelian dengan format sebagai berikut:
```python
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
```
### TERIMA KASIH
