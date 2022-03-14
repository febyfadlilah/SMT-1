def baju():
    Baju = 50000
    diskon = Baju*50/100
    hasil = Baju - diskon
    jumlah = int(input('Jumlah Pembelian = '))
    if jumlah > 0:
        bayar = jumlah*hasil
    print('Total Harga Baju = Rp. ',bayar)
def celana():
    Celana= 85000
    diskon = Celana*25/100
    hasil = Celana - diskon
    jumlah = int(input('Jumlah Pembelian = '))
    if jumlah > 0:
        bayar = jumlah*hasil
    print('Total Harga Celana Panjang = Rp. ',bayar)
def kaos():
    Kaos = 25000
    diskon = Kaos*15/100
    hasil = Kaos - diskon
    jumlah = int(input('Jumlah Pembelian = '))
    if jumlah > 0:
        bayar = jumlah*hasil
    print('Total Harga Kaos = Rp. ',bayar)
while True:
    print('SELAMAT DATANG DI TOKO FEBI BAHAGIA')
    print('='*100)
    print('Daftar Barang dan Harga\n1. Baju = Rp. 50000 diskon 50%\n2. Celana Panjang = Rp. 85000 diskon 25%\n3. Kaos = Rp. 25000 diskon 15%')
    pilih=int(input('Pilih Barang = '))
    if pilih == 1:
        baju()
    elif pilih == 2:
        celana()
    elif pilih == 3:
        kaos()
    