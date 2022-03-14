#buat matriks
def createMat2D (baris,kolom) :
    matriks = [ ]
    for i in range (baris) :
        isi = [ ]
        for y in range (kolom) :
            mat = int(input('matrik[' + str(i) + ',' + str(y) + ']= '))
            isi.append(mat)
        matriks.append(isi)
    return matriks
#nampilin matriks
def dispMat2D (matr,strmatr) :
    print (strmatr)
    if matr == False :
        print ('Ukuran Matriks Tidak Sama')
    else :
        for z in range (len(matr)) :
            print ('|',end='')
            for a in range (len(matr[1])) :
                data = str(matr[z][a])
                print (' '*(5-len(data))+ data,end='')
            print('    |')
#penjumlahan
def addMat (matriks1,matriks2) :
    if len(matriks1) == len(matriks2) and len(matriks1[0]) == len(matriks2[0]) :
        matriks = []
        for x in range (len(matriks1)) :
            hasil = []
            for f in range (len(matriks1[0])) :
                hasil.append (matriks1[x][f] + matriks2[x][f])
            matriks.append(hasil)
        return matriks
    else :
        return False

#perkalian
def multMat (matrik1,matrik2) :
    matriks = [ ]
    if (len(matrik1)) == (len(matrik2[0])) and (len(matrik1[0])) == (len(matrik2)) :
        for i in range (len(matrik1)) :
            hasil = []
            for u in range (len(matrik1)) :
                value = 0
                for a in range (len(matrik1[0])) :
                    value += matrik1[i][a] * matrik2[a][u]
                hasil.append(value)
            matriks.append(hasil)
        return matriks
    else :
        return False
                
# Main
print ('Create Mat 1')
matriks1 = createMat2D(2,3)
print ('Create Mat 2')
matriks2 = createMat2D(2,3)
print ('Create Mat 3')
matriks3 = createMat2D(3,2)
# tampilan matriks
hasilJumlah = addMat (matriks1,matriks2)
dispMat2D(matriks1,'Matrik1 =')
dispMat2D(matriks2,'Matrik2 = ')
dispMat2D(hasilJumlah,'Matriks1 + Matrik2 = ')

hasilJumlah = addMat (matriks1,matriks3)
dispMat2D(hasilJumlah,'Matriks1 + Matrik3 = ')
# perkalian
hasil = multMat (matriks1,matriks3)
dispMat2D(matriks1,'matrik1 = ')
dispMat2D(matriks3,'matrik3 = ')
dispMat2D(hasil,'hasil = ')

hasil2 = multMat (matriks1,matriks2)
dispMat2D(hasil2,'matrik1 * matrik 2 = ')
