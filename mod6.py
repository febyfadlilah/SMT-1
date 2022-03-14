def sumNumber(a,b):
    c=a+b
    print('Hasil Penjumlahan = ',c) 
def sumNumberReturn(a,b):
    c=a+b
    return c

num1=int(input('bilangan1= '))
num2=int(input('bilangan2= '))
sumNumber(num1,num2)
hasil=7*sumNumberReturn(num1,num2)
print(hasil)