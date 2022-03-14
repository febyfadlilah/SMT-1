data1 = [ ]
data2 = [ ]
jumlah = [ ]
matriks = 0
a = int(input('Banyaknya elemen Matriks - 1 = '))
for i in range (a) :
    print('Masukkan bilangan ke-',i,'=',end=' ')
    bil=int(input( ))
    data1.append(bil)
b = int(input('Banyaknya elemen Matriks - 2 = '))
for i in range (b) :
    print('Masukkan bilangan ke-',i,'=',end=' ')
    bilangan=int(input( ))
    data2.append(bilangan)
print ('Matriks 1 = ',data1)
print ('Matriks 2 = ',data2)
if len(data1) == len(data2) :
    matriks = len(data2)
    for i in range (matriks) :
        total = data1[i] + data2[i]
        jumlah.append(total)
    print ('Matriks 1 + Matriks 2 = ',jumlah)
else :
    print('Ukuran Matriks tidak sama')
