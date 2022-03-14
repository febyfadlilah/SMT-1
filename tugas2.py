sn = 0
a = int(input('Masukkan Suku Pertama : '))
b = int(input('Masukkan Beda Suku : '))
total = int(input('Masukkan Batas Total Deret Aritmatika : '))
for i in range (1,total) : 
    n = i
    un = a + (n-1)*b
    sn = sn + un
    if sn > total :  
        break
    print('Suku ke- ',i,': ',un,'Total= ',sn)