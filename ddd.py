start = True
while start :
    print('Menu \n1. Tekan 1 untuk konversi Desimal ke Biner\n2. Tekan 2 untuk konversi Biner ke Desimal')
    a = int(input('Masukkan Pilihan Anda : '))
    if a == 1 :
        b = int(input('Masukkan Desimal : '))
        hasilDiv=b
        while hasilDiv!=0 :
            hasilDiv=hasilDiv//2
            hasilMod=hasilDiv%2
            print(hasilMod)
    if a == 2 :
        c = int(input('Masukkan Biner : '))
        