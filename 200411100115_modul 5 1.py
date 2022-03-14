batas = int(input('Banyaknya bilangan = '))
bilangan = []
def createList (batas) :
    for i in range (batas) :
        bil = int(input('Masukkan data ke-' + str (i) + ' = '))
        bilangan.append(bil)
    return bilangan

genap = []
ganjil = []

def isGenap(bilangan) :
    return bilangan % 2 == 0

prima = []
def isPrime(bilangan) :
    if bilangan > 1:
        for i in range(2,bilangan):
            if bilangan % i == 0:
                return False
        else:
            return True
    else:
        return False

data = createList (batas)

for i in range (len(data)) :
    if isGenap(data[i]) and data [i] not in genap  :
        genap.append(data[i])
    if not isGenap(data[i]) and data [i] not in ganjil :
        ganjil.append (data[i])
    if isPrime(data[i]) and data[i] not in prima:
        prima.append(data[i])
        
print ('Bilangan = ',data)
print ('Genap = ',genap)
print ('Ganjil =',ganjil)
print('Prima = ',prima)