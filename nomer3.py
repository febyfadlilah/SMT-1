Nama = str(input("Masukkan Nama pegawai = "))
gol = int(input("Masukkan Golongan = "))
jam = int(input("Masukkan Jam Kerja = "))
if gol == 1 :
    if jam == 8 :
        print("hari ini anda tidak lembur, jadi upah harian anda Rp. 22500,-")
    if jam > 8 :
        lembur = jam - 8
        uanglembur = lembur * 4000
        upah = 22500 + uanglembur
        print("Hari ini anda lembur sebanyak ",lembur," jam, jadi upah anda hari ini adalah Rp.",upah)
if gol == 2 :
    if jam == 8 :
        print("hari ini anda tidak lembur, jadi upah harian anda Rp. 26000,-")
    if jam > 8 :
        lembur = jam - 8
        uanglembur = lembur * 4750
        upah = 26000 + uanglembur
        print("Hari ini anda lembur sebanyak ",lembur," jam, jadi upah anda hari ini adalah Rp.",upah)
if gol == 3 :
    if jam == 8 :
        print("hari ini anda tidak lembur, jadi upah harian anda Rp. 32500,-")
    if jam > 8 :
        lembur = jam - 8
        uanglembur = lembur * 6000
        upah = 32500 + uanglembur
        print("Hari ini anda lembur sebanyak ",lembur," jam, jadi upah anda hari ini adalah Rp.",upah)