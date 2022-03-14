uang = int(input('Masukkan uang anda : '))
pecahan = [100000,50000,20000,10000,5000,2000,1000]
strPecahan = ['seratus ribu','lima puluh ribu','dua puluh ribu','sepuluh ribu','lima ribu','dua ribu','seribu']

sisa = uang
start = True 
temp = 0
while start :
    bagi = sisa//pecahan[temp]
    print (bagi, 'lembar', strPecahan[temp])
    sisa = sisa % pecahan[temp]
    if sisa == 0 :
        start = False
    temp+=1