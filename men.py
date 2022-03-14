def faktorial (angka) :
    if angka == 1 :
        return 1
    else :
        return (angka*faktorial(angka-1))
def faktor (angka) :
    hasil = 1
    if angka == 1 :
        hasil = 1
    else :
        for i in range (1,angka+1) :
            hasil *= i
    return hasil,hasil

start = True
while start :
    pilih = int(input('Menu\n1. Iteratif\n2. Recursive\n3. Exit => ' )) 
    angka = int(input('masukkan angka : '))
    if pilih == 1 :
        faktor (angka)
    elif pilih == 2:
        faktorial (angka)
    else :
        start = False
    inp = str(input('Mau Ulang Lagi (y/t) : '))
    if inp == 'y' :
        start = True
    else :
        start = False


