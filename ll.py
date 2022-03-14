start = True 
while start :
    print('Pilih operasi \n1. penjumlahan \n2. pengurangan')
    pilih = int(input('pilihan '))
    a = int (input('Masukkan angka '))
    b = int (input('Masukkan angka '))
    if pilih == 1 :
        jumlah = a + b
        print(jumlah)
    else :
        kurang = a-b
        print (kurang)
    print('apakah ingin mengulang : 1. y / 2. t')
    inp=int(input('tanggapan : '))
    if inp == 1 :
        start = True
    else :
        start = False