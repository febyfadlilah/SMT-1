menu = ["pilih menu","makanan","minuman"]
makanan = {
	'permen' : 1000,
	'coklat' : 2000
}
minuman = {
	'sprite' : 3000,
	'susu' : 5000
}
barang = []
total_barang = []
total_harga = []
print ('='*100)
print (' '*30,'SELAMAT DATANG DI WARUNG MURAHSAE')
print ('='*100)
stop = False
while not(stop):
	print((menu[0]).upper())
	for i in range(1,len(menu)):
		print(f'{i}. {menu[i]}')
	inp = str(input('silahkan masukkan pilihan : '.upper(),  ))
	if inp.lower() == menu[1]:
		no = 1
		for i in makanan:
			print(f'{no}. {i}')
			no += 1
	elif inp.lower() == menu[2]:
		no = 1
		for i in minuman:
			print(f'{no}. {i}')
			no += 1
	inp1 = str(input('masukkan pilihan : '))
	barang.append(inp1)
	inp2 = int(input('masukkan jumlah : '))
	total_barang.append(inp2)
	if inp1 in makanan:
		total_harga.append(inp2 * makanan[inp1])
	elif inp1 in minuman:
		total_harga.append(inp2 * minuman[inp1])
	input_ulang = input('tambah belanjaan?(y/t)')
	if input_ulang == "y":
		stop = False
	else:
		print('Jumlah Harga =', sum(total_harga))
		jum_uang = int(input('Jumlah Uang : '))
		print('='*53*len(total_barang))
		print('barang yg dibeli', 'jumlah barang'.center(31), 'harga')
		for i in range(len(barang)):
			print(i+1, '.', barang[i], str(total_barang[i]).center(35), str(total_harga[i]).center(11))
		print('\n')
		print('Harga Total\t= ', ' '.center(14*2), sum(total_harga))
		print('uang anda\t= ', ' '.center(14*2), jum_uang)
		kembalian = jum_uang - sum(total_harga)
		print('kembalian anda\t=', ' '.center(14*2+1), kembalian)
			
		stop = True