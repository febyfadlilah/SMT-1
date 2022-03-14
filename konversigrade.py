#konversi nilai angka 

grade=int(input('Masukkan Nilai = '))
if grade == 0 :
    print('Nilai anda 0, dan biaya yang harus dikeluarkan Rp.550.000,-')
if grade>0 and grade<=39 :
    print('Nilai anda E, dan biaya yang harus dikeluarkan Rp.450.000,-')
if grade>=40 and grade<=59 :
    print('Nilai anda D, dan biaya yang harus dikeluarkan Rp.350.000,-')
if grade>=60 and grade<=75 :
    print('Nilai anda C, dan biaya yang harus dikeluarkan Rp.250.000,-')
if grade>75 and grade<=90 :
    print('Nilai anda B, dan biaya yang harus dikeluarkan Rp.150.000,-')
if grade >90 and grade<=100 :
    print('Nilai anda A, dan biaya yang harus dikeluarkan Rp.50.000,-')