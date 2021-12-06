#membuat variable
Data = 'nomor'
data_baru = Data + ' (Hasil)'
data_awal = open(Data, 'r')
data_akhir = open(data_baru, 'w')

#membaca data
while True:
      baca_data = data_awal.readline()
      if not baca_data:
         data_awal.close()
         data_akhir.close()
         break
      #mengganti tanda '|' dengan '+' dan dijumlahkan
      pisah_data = baca_data.split('|')
      pisah_data[1] = pisah_data[1].replace('\n', ' ')
      sum = int(pisah_data[0])+int(pisah_data[1])
      data_akhir.write(str(sum)+'\n')
      print(' + '.join(pisah_data), '=', sum)

print('\n[Hasil penjumlahan disimpan dalam file', data_baru + ']\n')
