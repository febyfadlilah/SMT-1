bil=int(input('Masukkan Bilangan: '))
#prima hanya bisa dibagi dengan 1 dan bilangan itu sendiri
if bil >= 2:
    bagi=0
    for i in range (1,bil+1):
        if bil % i== 0 :
            bagi += 1   
    if bagi == 2 :
        print('Merupakan Bilangan Prima')
    else:
        print('Adalah Bukan Bilangan Prima')
else:
    print('Adalah Bukan Bilangan Prima')
