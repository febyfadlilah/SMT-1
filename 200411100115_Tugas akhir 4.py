#  FEBI FADLILAH NUR AMINAH

mulai = True
print('searching Data in list')
print(' ')
data = ["if", "you","rerun", "the", "analysis", "using", "our", "algoritms", "and", "our", "data", "you", "will","not", "get", "the", "identical", "result", "as", "provided", "here", "the","reason","is","an","inherent","stochastic","component","in","these","result","all","test","are","based","on","surrogates","surrogates","are","random","signal"]
while mulai :
    kata = str(input('Masukkan Data yang mau dicari = '))
    i = 0
    x = 0
    for f in data :
        if f == kata.lower() :  
            print('data',kata,'ada di index ke - ',i)
            x += 1
        i += 1
    if kata.lower() not in data:
        print('Data tidak ditemukan')
    if x > 0 :
        print('Jumlah data ',kata,'sebanyak = ',x)
    cari = str(input('y untuk cari lagi = '))
    if cari.lower() == 'y' :
        mulai = True
    else :
        mulai = False

