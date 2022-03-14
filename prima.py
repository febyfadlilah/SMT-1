#bilangan prima atau bukan
bil=int(input('Masukkan Bilangan: '))
if bil >= 2:
    for i in range(2,bil):
         if (bil % i) == 0:
             print ('Adalah Bukan Bilangan Prima')
             break
    else:
         print('Merupakan Bilangan Prima')


else:
    print('Adalah Bukan Bilangan Prima')


# kalau tidak di break maka akan muncul 2 print contoh angka 4 dia masuk ke loop sisa 0 jika dibagi 2 
# dan dia keluar loop sisa 1 jika dibagi 3 karena range nya ada pada (2-4), angka didalamnya adalah (2,3,4)