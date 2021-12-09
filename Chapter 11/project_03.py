from datetime import *
data = open('data_perpus.txt', 'r')

def terlambat(x):
    date = datetime.strptime(str(x), '%Y-%m-%d')
    sekarang = datetime.now()
    selisih = sekarang - date
    return selisih.days

cari = input("[Silakan cari data member]\nMasukkan kode member: ")

while True:
      read_data = data.readline()
      split_data = read_data.split('|')
      if cari == split_data[0]:
         beda_waktu = terlambat(split_data[4].replace('\n', ''))
         if beda_waktu < 0:
            beda_waktu = 0
         print('='*42)
         print('Data Peminjaman Buku'.center(42))
         print('='*42, '\n')
         print("Kode Member\t\t: ", split_data[0])
         print("Nama Member\t\t: ", split_data[1])
         print("Nama Buku\t\t: ", split_data[2])
         print("Tanggal Mulai Peminjaman: ", split_data[3])
         print("Tanggal Maks Peminjaman\t: ", split_data[4].replace('\n', ''))
         print("Tanggal Pengembalian\t: ", datetime.date(datetime.now()))
         print("Terlambat\t\t: ", beda_waktu, "hari")
         print("Denda\t\t\t:  Rp", 2000 * beda_waktu)
         print("-"*42, '\n')
         break

      if not read_data:
         data.close()
         print("\n[Data Not Found]\n")
         break
