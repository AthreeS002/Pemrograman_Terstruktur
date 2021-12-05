jumlah = []
data = int(input('Berapa kali ingin mengurutkan angka?: '))
for n in range(data):
    angka = int(input('Masukkan angka: '))
    jumlah.append(angka)
jumlah.sort(reverse=True)
print("urutan angkanya adalah :"+ str(jumlah))
