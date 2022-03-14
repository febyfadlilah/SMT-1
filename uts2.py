vokal = 0
voc =''
spasi = 0
spas = ''
konsonan = 0
kons = ''
a = str(input("masukkan Kata => "))
for i in a:
    if i == "a" or i == "A" or i == "i" or i == "I" or i == "u" or i == "U" or i == "e" or i == "E" or i == "o" or i == "O":
        voc += i
        voc += ' '
        vokal += 1
    elif i == ' ':
        spasi += 1
    else:
        konsonan += 1
        kons += i
        kons += ' '
        
print("Jumlah Huruf Vokal = ",vokal,",","Yaitu :",voc)
print("Jumlah Huruf Konsonan = ",konsonan,",","Yaitu :",kons)
print("Jumlah Spasi = ",spasi)
