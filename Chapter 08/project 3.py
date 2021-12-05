try:
    print()
    jumlah = int(input('Masukkan jumlah nama yang ingin di-input: '))
    print()
    print('-----------------------------------------')
    list_nama = []

    for i in range(jumlah):
        nama = input('Masukkan nama ke-'+str(i+1) + ': ')
        list_nama.append(nama)

    list_nama.sort()

    print('-----------------------------------------')
    for nama in list_nama:
        print(nama, '('+str(len(nama)), 'karakter)')
except ValueError:
    print('[Input Salah]')
