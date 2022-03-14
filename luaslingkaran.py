#menghitung luas lingkaran 
while True:
    print('Luas Lingkaran\n1. Jari-jari bukan kelipatan 7\n2. Jari-jari kelipatan 7')
    pilih=int(input('pilih opsi = '))
    if pilih == 1:
        r=float(input('masukkan nilai jari-jari = '))
        area=3.14*r*r
        print('jari-jari',r,'luas lingkaran',area)
        break
    else:
        r=float(input('masukkan nilai jari-jari = '))
        area=22/7*r*r
        print('jari-jari',r,'luas lingkaran',area)
        break