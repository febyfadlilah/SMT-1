x = int(input('Masukkan Bilangan = '))
n = int(input('Masukkan pangkat yang di inginkan = '))
def operasi (x,n) :
    if n == 0 :
        return 1
    else :
        pangkat = x * operasi (x,n-1)
        return pangkat

print('Bilangan ',x,' jika dipangkatkan ',n,' hasilnya = ',operasi(x,n))