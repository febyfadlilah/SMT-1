# 2, 4, 6, 8, 10, 12, ....
#Un=a+(n-1)b
Sn=0
a = 2
b = 2
for i in range (10):
    n=i+1
    un=a+(n-1)*b
    print(un)
    Sn=Sn+un
print('Jumlah Angka', Sn)