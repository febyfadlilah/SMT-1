data = [90,56,34,78,86,100,87,88,75,65,86,57,89,67,80]
a = int(input('Masukkan angka : '))
for nilai in range (0,len(data)) :
    if a<data[nilai] :
        print('index ke-',nilai)