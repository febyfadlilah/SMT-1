jumlah = 0
a = str(input('Masukkan kalimatmu : '))
for i in a :
    if i == 'a' or i == 'i' or i == 'u' or i == 'e' or i == 'o' :
        jumlah += 1
        print(i,end=' ')
    else :
        jumlah += 1
        print(i)
print ('jumlah huruf vokal ada ',jumlah)