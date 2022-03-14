x = int(input('Masukkan Bilangan = '))
n = int(input('Masukkan pangkat yang di inginkan = '))

def operasi (x,n) :
    if n == 0 :
        pangkat = 1
    else :
        a = 0
        pangkat = 1
        while a < n :
            pangkat *= x
            a += 1
    return pangkat

hasil = operasi(x,n)
print('Bilangan ',x,' jika dipangkatkan ',n,' hasilnya = ',hasil)