golA = 10000000
golB = 8500000
golC = 7000000
golD = 5500000

kode = int(input("Masukkan kode karyawan: "))
nama = input("Masukkan nama karyawan: ")
gol = input("Masukkan golongan: ")
print()


print("======================================")
print("     STRUK RINCIAN GAJI KARYAWAN")
print("--------------------------------------")
print()

print("Nama Karyawan       :", nama, ("(kode :"+str(kode)+")"))
print("Golongan            :", gol)
print("--------------------------------------")

#memberi def gaji pokok
def gajii(gol):
    if gol == 'A':
       return golA
    elif gol == 'B':
       return golB
    elif gol == 'C':
       return golC
    elif gol == 'D':
       return golD
    else:
       print("Hanya ada golongan A, B, C dan D")
       exit()

#memberi potongan sesuai golongan
def bersih1(gol):
    if gol == 'A':
       print ("Gaji Pokok          : Rp", golA)
       print ("Potongan 2.5%       : Rp", int(golA * 2.5/100))
       return golA * 2.5/100
    elif gol == 'B':
       print ("Gaji Pokok          : Rp", golB)
       print ("Potongan 2.0%       : Rp", int(golB * 2/100))
       return golB * 2/100
    elif gol == 'C':
       print ("Gaji Pokok          : Rp", golC)
       print ("Potongan 1.5%       : Rp", int(golC * 1.5/100))
       return golC * 1.5/100
    elif gol == 'D':
       print ("Gaji Pokok          : Rp", golD)
       print ("Potongan 1.0%       : Rp", int(golD * 1/100))
       return golD * 1/100


gaji = (gajii(gol))
hasil = int(bersih1(gol))
gbersih = gaji - hasil

#print("Potongan            : Rp", int(hasil))
print("------------------------------------- -")
print("Gaji Bersih         : Rp", gbersih)
