def bilangan_prima(angka):
    prima = []
    bprima = []
    for i in range(1,angka+1,2):
        if i == 1:
            bprima.append(i)
        else:
            for x in range(2,i):
                if i % x == 0:
                    bprima.append(i)
                    break
            else:
                prima.append(i)
    return prima,bprima
a,b = bilangan_prima(20)
print('prima',a)
print('bukan prima',b)