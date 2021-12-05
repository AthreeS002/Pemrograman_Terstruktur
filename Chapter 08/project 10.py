def tampilkan_data(data):
    print('----------------------')
    print('Daftar Buah: ')
    for key, value in data.items():
        print('-', key, ':', value)


buah = {'Apel': 5000,
        'Jeruk': 8500,
        'Mangga': 7800,
        'Duku': 6500}


tampilkan_data(buah)

total_semua = 0
while True:
    try:
        print('----------------------')
        nama = input('Masukkan nama buah: ')
        harga = buah[nama]
        jumlah = int(input('Berapa Kilogram?  : '))
        total_harga = harga * jumlah
        total_semua += total_harga
        tambah = input('\nBeli buah yang lain (y/n)?: ')
        if tambah == 'n' or tambah == 'N':
            print('======================')
            print('Total harga  =', total_semua)
            break
    except KeyError:
        print('\n[Data Error]')
