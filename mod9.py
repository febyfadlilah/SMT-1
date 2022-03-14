def cekGenap(bil):
    if bil%2==0:
        print('Genap')
    else :
        print('Ganjil')

num=int(input('masukkan bilangan = '))

print(cekGenap(num))
if cekGenap(num):
    hasil=num*3
else :
    hasil=num*2
print(hasil)