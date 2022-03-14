# menentukan bilangan fibonacci
angka1 = 0
angka2 = 1

batas=int(input('Masukkan Batas Angka= '))
for i in range(batas):
    print(angka1,end=',')
    angkax = angka1 + angka2
    angka1 = angka2
    angka2 = angkax