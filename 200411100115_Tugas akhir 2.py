#  FEBI FADLILAH NUR AMINAH
print('---/// Program menginputkan angka kedalam jam digital ///---')
start = True
while start : 
    jam = 0
    menit = 0
    detik = 0
    hours = int(input('Masukkan jam = '))
    if hours < 24 :
        jam += hours
        minutes = int(input('Masukkan menit = '))
        if minutes >= 60 :
            jam = hours + 1
            if jam == 24 :
                jam -= 24
            menit += (minutes-60)
        else :
            menit += minutes
        second = int(input('Masukkan detik = '))
        if second >= 60 :
            minutes += 1
            detik += (second-60)
        else :
            detik += second
    
        print('Jam %s : %s : %s'%(str(jam).zfill(2),str(menit).zfill(2),str(detik).zfill(2)))
        ulang = str(input('Mau coba lagi (y/t) = '))
        if ulang == 'y' :
            start = True
        else :
            start = False
    else :
        print('Jam tidak boleh lebih dari 23')
        start = False
print('---/// SELESAI ///---')