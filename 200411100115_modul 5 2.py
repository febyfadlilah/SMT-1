angka = int(input('Masukkan Angka : '))
def pembagi(angka):
    pembagi = []
    for i in range(1,angka+1):
        if angka % i == 0:
            pembagi.append(i)
    return pembagi

faktor = pembagi (angka)
print ('Bilangan Pembagi = ',faktor)