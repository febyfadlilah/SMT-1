#  FEBI FADLILAH NUR AMINAH

def triangularNumbers (n) :
    if n == 1 :
        hasil = 1
    else :
        hasil = n + triangularNumbers (n-1)
    return hasil

jumlah = triangularNumbers (4)
print ('hasil dari triangularNumbers = ',jumlah)