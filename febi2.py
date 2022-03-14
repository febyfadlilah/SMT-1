temp=0
number=int(input('Masukkan Angka Maksimal= '))
for i in range(number):
    if i%2==1:
        temp= temp+i
        print('bilangan ganjil=',i)
print('Total Angka', temp)
