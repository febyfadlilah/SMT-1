x = int(input('Masukkan Bilangan = '))
n = int(input('Masukkan pangkat = '))

def expNumber (x,n) :
    if n == 0 :
        pangkat = 1
    else :
        a = 0
        pangkat = 1
        while a < n :
            pangkat *= x
            a += 1
    return pangkat

hasil = expNumber (x,n)
print(x,' pangkat ',n,' = ',hasil)