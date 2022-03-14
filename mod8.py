def cekPrima(bil):
    count=0
    for i in range(bil):
        if bil%(i+1)==0:
            count=count+1
    print(count)
    if count==2:
        return True
    else :
        return False

cekPrima(5)