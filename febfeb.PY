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