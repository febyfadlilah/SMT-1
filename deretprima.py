n = int(input('Masukkan jumlah = '))
jumlah = 0
awal = 2

while jumlah < n :
    prima = True
    for i in range (2,awal) :
        if awal % i == 0 :
            prima = False
    if (prima) :
        print (awal,end=',')
        jumlah += 1
    awal += 1