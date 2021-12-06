data = open('data mhs.txt', 'r')

cari = input('\nMasukkan NIM yang ingin dicari: ')
while True:
      read_file = data.readline()
      split_data = read_file.split('|')
      if cari == split_data[0]:
         print('\n' + '='*39)
         print('Data Mahasiswa'.center(39))
         print('='*39, '\n')
         print('NIM        : ', split_data[0])
         print('Nama       : ', split_data[1])
         print('Alamat     : ', split_data[2])
         print('-'*39, '\n')
         break
         
      if not read_file:
         print('\n[Data Tidak Ditemukan!]\n')
         data.close()
         break
