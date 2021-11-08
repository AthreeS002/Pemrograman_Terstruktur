def namaFile():
       global nama

       try:
           nama = input("Masukkan nama File: ")
           file = open(nama, "r")
       except FileNotFoundError:
           exit("File tidak ditemukan")

def read():
    file = open(nama, "r")
    print('Isi dari file', nama, 'adalah:\n')
    print(file.read())
    
def write():
    file = open(nama, "a")
    tambah = input("Tambahkan data: ")
    file.write(tambah)
    
    if len(tambah) >= 0:
       file.write('\n')
    

namaFile()
read()
while True:
      respon = input("Apakah ingin mengubah data? Y/N: ")
      if respon == 'y' or respon == 'Y':
         write()
         read()
      elif respon == 'n' or respon == 'N':
         read()
      else:
         print("harap jawab Y/N saja", '\n')
         continue
      
      skip = input("Apakah anda ingin lanjut? Y/N: ")
      if skip == 'Y' or skip == 'y':
         ()
      elif skip == 'N' or skip == 'n':
         print("exit")
         break
      else:
         print("Harap jawab Y/N saja", '\n')
         
         
         
