start = True
while start:
    jumlah = 0
    a = str(input('Masukkan data : '))
    b = str(input('Masukkan huruf yang dicari : ' ))
    for i in a :
        if i == b :
            jumlah = jumlah + 1
            print(i,end=',')
    print('Jumlahnya : ',jumlah)
    print('Apakah mau mencari lagi ? 1. ya / 2. tidak')
    opsi = int(input('Pilih opsi : '))
    if opsi == 1 :
        start = True
    else :
        start = False
    print(' ')
