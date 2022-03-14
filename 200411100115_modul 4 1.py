bilangan = [ ]
genap = [ ]
ganjil = [ ]
prima = [ ]
a = int(input('Masukkan Bilangan : '))
for i in range (a) :
    print('Masukkan bilangan ke-',i,'=',end=' ')
    bil=int(input( ))
    bilangan.append(bil)
for i in bilangan :
    if i % 2 == 0 and i not in genap: 
        genap.append(i)
    elif i % 2 == 1 and i not in ganjil:
        ganjil.append(i)
bagi = 0
for i in bilangan:
    for y in range (1,i+1) :
        if i % y == 0 :
            bagi += 1
    if bagi == 2 and i not in prima:
        prima.append(i)
    bagi = 0
print('Bilangan=',bilangan)
print('Genap=',genap)
print('Ganjil=',ganjil)
print('Prima=',prima)
