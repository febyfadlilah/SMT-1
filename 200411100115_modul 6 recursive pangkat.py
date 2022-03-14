x = int(input('Masukkan Bilangan = '))
n = int(input('Masukkan pangkat = '))
def expNumber (x,n) :
    if n == 0 :
        return 1
    else :
        pangkat = x * expNumber (x,n-1)
        return pangkat
hasil = expNumber (x,n)
print(x,' pangkat ',n,' = ',hasil)