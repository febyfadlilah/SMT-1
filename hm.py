temp = 0
x = 0
data = [90,56,34,78,86,90,87,88,75,65,86,57,89,67,80]
for nilai in data :
    if nilai % 2 == 1 :
        x = x + 1
        print (nilai)
        temp = nilai + temp
print ('jumlahnya ',temp)
rata = temp/x
print('rata-ratanya ',rata)
mimi = max(data)
print (mimi)