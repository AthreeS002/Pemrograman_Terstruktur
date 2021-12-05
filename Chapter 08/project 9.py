def tampilkan_data(data):
    for key, value in data.items():
        print('- ' + key, ':', value)


buah = {'Apel': 5000,
        'Jeruk': 8500,
        'Mangga': 7800,
        'Duku': 6500}

tampilkan_data(buah)
print()
try:
    print('-------------------------')
    nama = input('Masukkan nama buah: ')
    harga = buah[nama]
    jumlah = int(input('Berapa Kilogram?  : '))
    total_harga = jumlah * harga
    print('-------------------------')
    print('Total harga       =', total_harga)

except KeyError:
    print('\n[Data Error]')
