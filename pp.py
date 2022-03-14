b = str (input('masukkan romawi : '))
romawi = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
asli=[1000,900,400,100,90,50,40,10,9,5,4,1]
angka= ' '
for i in range (len(romawi)) :
    while b>= romawi[i] :
        b -= romawi[i]
        angka += asli [i]
print(angka)
