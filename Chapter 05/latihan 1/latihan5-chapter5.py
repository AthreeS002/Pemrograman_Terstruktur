#mendefinisikan gaji pokok
golA = 10000000
golB = 8500000
golC = 7000000
golD = 5500000

#menginputkan data
kode = int(input("Masukkan kode karyawan           : "))
nama = input("Masukkan nama karyawan           : ")
gol = input("Masukkan golongan                : ")
stt = int(input("Masukkan status (1: menikah, 2: blm)   : "))
#perbedaan menikah dan tidak
if stt == 1:
   status = "Menikah"
   anak = int(input("Masukkan jumlah anak: "))
elif stt == 2:
   status = "Belum Menikah"
   anak = 0
   ()
else:
   exit("Hanya ada dua pilihan")

print()

#output
print("======================================")
print("     STRUK RINCIAN GAJI KARYAWAN")
print("--------------------------------------")
print()

print("Nama Karyawan       :", nama, ("(kode :"+str(kode)+")"))
print("Golongan            :", gol)
print("Status Menikah      :", status)

print("Jumlah Anak	    :", anak)
print("--------------------------------------")

#memberi def output gaji pokok sesuai golongan
def gpokok(gol):
    if gol == 'A':
       print ("Gaji Pokok          : Rp", golA)
       return golA
    elif gol == 'B':
       print ("Gaji Pokok          : Rp", golB)
       return golB
    elif gol == 'C':
       print ("Gaji Pokok          : Rp", golC)
       return golC
    elif gol == 'D':
       print ("Gaji Pokok          : Rp", golD)
       return golD
       
#memberi def potongan sesuai golongan
def potongan(gol):
   if gol == 'A':
      return int(golA * 2.5/100)
   elif gol == 'B':
      return int(golB * 2/100)
   elif gol == 'C':
      return int(golC * 1.5/100)
   elif gol == 'D':
      return int(golD * 1/100)

Gpokok = gpokok(gol)
potongan = potongan(gol)

#memberi def tunjangan menikah
def tnjMenikah(Gpokok):
    if stt == 1:
       return Gpokok * 10/100
    elif stt == 2:
       return 0
    else:
       ()
       
def tnjAnak(Gpokok):
    return anak * (Gpokok * 5/100)

#menghitung rumus
tnjMenikah = tnjMenikah(Gpokok)
tnjAnak = tnjAnak(Gpokok)
gajikotor = int(Gpokok + tnjMenikah + tnjAnak)
gbersih = gajikotor - potongan
    
#output tunjungan
print("Tunjangan Menikah   : Rp", int(tnjMenikah))
print("Tunjangan anak      : Rp", int(tnjAnak))

#output hasil total
print("------------------------------------- +")
print("Gaji Kotor          : Rp", gajikotor)
if gol == 'A':
   print("Potongan 2.5%       : Rp " +str(int(golA * 2.5/100)))
      
elif gol == 'B':
   print("Potongan 2.0%       : Rp " +str(int(golB * 2/100)))

elif gol == 'C':
   print("Potongan 1.5%       : Rp " +str(int(golC * 1.5/100)))

elif gol == 'D':
   print("Potongan 1.0%       : Rp " +str(int(golD * 1/100)))
print("------------------------------------- -")
  
#print(potongan)
print("Gaji Bersih         : Rp", gbersih)
