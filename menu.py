while True :
    print('Menu\n1. Perhitungan Luas Lingkaran\n2. Perhitungan Luas Persegi Panjang\n3. Perhitungan Luas Segitiga')
    a =int(input('Masukkan Pilihan Anda : '))
    if a == 1 :
        r = int(input('Masukkan Jari-jari : '))
        luas = 22/7*r*r
        print('Luas Lingkaran Anda : ',luas)
    elif a == 2 :
        p = int(input('Masukkan panjang : '))
        l = int(input('Masukkan lebar : '))
        luas = p * l
        print('Luas Persegi Panjang Anda : ',luas)
    else :
        alas = int(input('Masukkan panjang alas : '))
        t = int(input('Masukkan Tingi : '))
        luas = 1/2 *alas*t
        print('Luas Segitiga Anda : ',luas)
    print('Ingin mengulang Operasi kembali (1. y/2. t)')
    inp = int(input('Pilih Opsi : '))
    if inp == 1 :
        continue
    else :
        break
