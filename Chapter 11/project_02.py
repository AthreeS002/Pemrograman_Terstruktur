from datetime import *

data_perpus = open('data_perpus.txt', 'a+')
awal = datetime.date(datetime.now())
akhir = awal + timedelta(days =+ 7)

while True:
      member = input("Masukkan kode member: ")
      nama = input("Masukkan nama: ")
      judul = input("Masukkan judul buku: ")
      data_perpus.write(member + '|' + nama + '|' + judul + '|' + str(awal) + '|' + str(akhir) + '\n')
      opsi = input("\nIngin input lagi? (y/n): ")
      if opsi == 'n' or opsi == 'N':
         data_perpus.close()
         print("\n[Saving ... ]\n[Exit]\n")
         break
      else:
         continue

