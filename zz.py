def pangkat (x,n) :
    temp = 0
    if n == 0 :
        temp = 1
    else :
        for i in range (n) :
            temp = temp * x
    return temp


x = int(input('Masukkan Bilangan = '))
n = int(input('Masukkan pangkat  = '))
print(x,' pangkat',n,'=',pangkat(x,n))
