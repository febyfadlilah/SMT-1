# FEBI FADLILAH NUR AMINAH (200411100115)
nama = [ ]
nilai = [ ]
a = int(input('Masukkan jumlah mahasiswa : '))
for i in range (1,a+1) :
    print ('mahasiswa ke-',i)
    name=input('Masukkan Nama Mahasiswa : ')
    nama.append(name)
    value=int(input('Masukkan Nilai Mahasiswa : '))
    nilai.append(value)
print('-'*50)
start=True
while start :
    print("Data Nilai Mahasiswa")
    print("Tekan 0 untuk Daftar keseluruhan mahasiswa dan nilainya")
    print("Tekan 1 perhitungan rata-rata")
    print("Tekan 2 untuk  mahasiswa dengan nilai lebih dari threshold")
    print("Tekan 3 nilai tertinggi")
    b = int(input('Masukkan Pilihan Anda => '))
    if b == 0 :
        urutan = 0
        for data in range (len(nama)) :
            urutan = urutan + 1
            print(urutan,'.',nama[data],':',nilai[data])
    elif b == 1 :
        juml = 0
        for rata in nilai:
            juml += rata
        print("rata-rata nilai =",juml/len(nilai))
    elif b == 2 :
        temp = 0
        thres= int(input('Masukkan Angka : '))
        print('Nilai yang lebih besar dari ',thres,' adalah ')
        for i in nilai :
            if i > thres :
                print(nama[temp],':',nilai[temp])
            temp +=1
    else :
        maksimal = nilai[0]
        for i in range (len(nilai)):
            if maksimal < nilai[i]:
                maksimal = nilai[i]
        print('Nilai Tertinggi adalah :',maksimal)

    tanggapan = str(input('Apakah Ingin Mencari Yang Lain ? (y/t) = '))
    if tanggapan == 't' :
        start = False
    print('-'*50)




