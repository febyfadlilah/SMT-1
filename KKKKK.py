import febfeb as matr
print('create matriks 1')
matriks1 = matr.createMat2D(3,3)
print('create matriks 2')
matriks2 = matr.createMat2D(3,3)
# print matriks
matr.dispMat2D(matriks1, 'matriks 1')
matr.dispMat2D(matriks2, 'matriks 2')
# perkalian matriks
kali = matr.multMat(matriks1,matriks2)
# print matriks
matr.dispMat2D(kali, 'matriks 1 * matriks 2')