bilangan = 1
counter = 1
a= int(input('Masukkan batas angka : '))
while counter <= a :
    if bilangan % 2 == 0 :
        print ('bil genap-',counter,'=',bilangan)
        counter+=1
    bilangan+=1
print('Finished')