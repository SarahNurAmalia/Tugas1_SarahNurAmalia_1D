# Input data pengguna

nama_penguna = str(input('Masukkan Nama Pengguna: '))
waktu_pengguna = float(input('Masukkan Waktu Pembelian (dalam detik): '))
stok_produk = int(input('Masukkan Jumlah Stok Produk: '))
pembayaran = str(input('Pilih Metode Pembayaran: '))
harga = int(input('Masukkan Total Harga: '))

# Metode Pembayaran dan batas waktu maksimal untuk "war" 

sistem_pembayaran = ['COD']
batas_waktu = 5.0
admin = 1000
total_harga = admin + harga

# #Logika untuk menentukan hasil "war"
hasil = 'Selamat Pembelian Berhasil' if (stok_produk <= 10) and (waktu_pengguna <= batas_waktu) and (harga >= 50000) and (pembayaran not in sistem_pembayaran) else 'Maaf, Pembelian Anda Gagal'
print(f'Total Harga (termasuk admin): {total_harga}')
print(hasil)