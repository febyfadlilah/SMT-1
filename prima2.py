jumlah = int(input('masukkan batas: '))
i = 2
while i in range (i,jumlah) :
    j = 2
    prima = True
    while j < i :
        if (i % j == 0):
            prima = False
            break
        j = j + 1
    if (prima) :
        print (i,end=' ')
    i = i + 1