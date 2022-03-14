a = int(input("Masukkan Angka pertama = "))
b = int(input("Masukkan Batas angka = "))
for i in range (a,b+1) :
    if i % 2 == 1 :
        print ("Angka ganjil ",i)
    else :
        print("Angka genap ",i)
