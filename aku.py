while True :
    data = 'jelasin secara benar'
    ch=input('masukkan data = ')
    counter = 0
    for karakter in data :
        if karakter == ch :
            counter+=1
    print(counter)
    inp = input('stop ? (y/t) = ')
    if inp == 'y' :
        break
    else :
        continue