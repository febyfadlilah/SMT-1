# FEBI FADLILAH NUR AMINAH (200411100115)
n = 0
maksimal = 0
a = int(input('Masukkan bilangan pertama : '))
b = int(input('Masukkan bilangan kedua : '))
for i in range (2,a+1 and b+1) :
    if a % i== 0 and b % i == 0 :
        n=n+1
        print ('Pembagi yang sama-',n,'= ',i)
        maksimal = i
print ('Pembagi yang sama terbesar = ',maksimal)