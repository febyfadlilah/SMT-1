def operasi (a,b,pilih) :
    if pilih == 1 :
        hasil = a+b
    elif pilih == 2 :
        hasil = a-b
    elif pilih == 3 :
        hasil = a*b
    else :
        hasil = a/b
    return hasil

def display (hasil) :
    print('nilai = %5d'%hasil)

start = True
while start :
    print('Pilih Operasi\n1. Penjumlahan\n2. Pengurangan\n3. Perkalian\n4. Pembagian')
    pilih = int(input('Masukkan Pilihan anda = '))
    a = int(input('Masukkan Angka pertama : '))
    b = int(input('Masukkan Angka Kedua : '))
    hasil = operasi (a,b,pilih)
    display (hasil)
    ulang = input('Mau ulang lagi (y/t)')
    if ulang == 'y' :
        start = True
    else :
        start = False