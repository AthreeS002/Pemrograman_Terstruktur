data = open('data mhs.txt', 'a+')

#menambahkan data baru
while True:
    NIM = input('Masukkan NIM\t: ')
    Nama = input('Masukkan Nama\t: ')
    Alamat = input('Masukkan Alamat\t: ')

    data.write(NIM + '|' + Nama + '|' + Alamat + '\n')

    tambah_data = input('\nUlangi input lagi? (y/n)\t: ')
    print('')
    
    if (tambah_data == 'y' or tambah_data == 'Y'):
       continue
    elif (tambah_data == 'n' or tambah_data == 'N'):
        print('[Exit]\n')
        break
    else:
        print('\n[Hanya bisa Y/N]')
        break

#membaca data baru
data.seek(0, 0)
isi = data.read()
print(isi)

data.close()
