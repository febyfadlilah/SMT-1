jenis = int(input("Masukkan jenis kendaraan anda\n1. Sepeda motor\n2. Mobil\n3. Masukkan (1/2) ="))
mnt = int(input("Berapa menit anda parkir ? "))
if jenis == 1 :
    if mnt == 60 :
        print("Tarif parkir anda Rp. 5000")
    if mnt >= 60 :
        menit = mnt - 60
        men = menit//15
        trf = men*1000
        tarif = 5000 + trf
        print("tarif parkir anda Rp.",tarif)
else :
    if mnt == 60 :
        print("Tarif parkir anda Rp. 10000")
    if mnt >= 60 :
        menit = mnt - 60
        men = menit//15
        trf = men*2000
        tarif = 10000 + trf
        print("tarif parkir anda Rp.",tarif)