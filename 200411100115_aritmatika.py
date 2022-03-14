sn = 0
un = 0
n = 0
a = int(input('Masukkan Suku Pertama : '))
b = int(input('Masukkan Beda Suku : '))
total = int(input('Masukkan Batas Total Deret Aritmatika : '))
while (sn + un) < total : 
    n = n + 1
    un = a + (n-1)*b
    sn = sn + un
    print('Suku ke- ',n,'= ',un,'Total = ',sn)