password='tanggalLahirku'

def setPassword3():
    password='namaku'
    return password
#tambah return password
def displayPassword3(password):
    print('the password is',password)
# varibel global tidak terbaca jika menggunkan parameter
data = setPassword3()
displayPassword3(data)