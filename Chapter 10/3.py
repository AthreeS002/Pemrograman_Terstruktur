Data = open('data mhs.txt', 'r')

data_mhs = list()
while True:
      Data_read = Data.readline()
      if not Data_read:
         Data.close()
         break
      
      data_split = Data_read.split('|')
      enter = len(data_split) - 1
      data_split[enter] = data_split[enter].replace('\n', '')
      
      data = dict()
      data['NIM'] = data_split[0]
      data['Nama'] = data_split[1]
      data['Alamat'] = data_split[2]
      data_mhs.append(data)

print('Data Mahasiswa = ', data_mhs)
