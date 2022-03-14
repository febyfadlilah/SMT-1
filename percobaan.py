# 2, 4, 6, 8, 10, 12, .....

a=2
temp=0
batas=int(input('Masukkan Angka Maksimal= '))
for i in range (batas):
    print(a)
    temp=temp+a
    a=a+2
print('total= ',temp)