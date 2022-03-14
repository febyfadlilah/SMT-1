total=0
def jumlah(a,b):
    c=a+b
    global total
    total=total+c

jumlah(6,7)
print(total)