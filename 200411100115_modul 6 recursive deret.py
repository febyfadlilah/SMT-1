a = int(input('Masukkan Suku Awal = '))
b = int(input('Masukkan Beda = '))
n = int(input('Masukkan Banyaknya Suku = '))

def deret (a,b,n) :
    if n == 1 :
        return a
    else :
        un = b + deret (a,b,n-1)
        return un
hasil = deret (a,b,n)
print('Suku ke - ',n,' = ',hasil)