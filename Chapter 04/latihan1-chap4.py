print("==========================================================")
print("                    Rental Mobil Ad")
print("==========================================================")
print("")
hrg = 200000
hrgT = 10000

print("Tarif biaya selama 12 jam awal: Rp", hrg, ",-")
print("Tarif biaya tambahan per jam: Rp", hrgT, ",-")
print()

print("Apakah Anda ingin melanjutkan?")
print("Y: lanjut")
print("N: batal")
stj = input("Option = ")
if stj == 'Y':
   ()
elif stj == 'N':
   exit("Terimakasih sudah berkunjung!! ^_^")
else:
   print("Tolong masukkan huruf Y/N saja")
   exit()

print("_______________________________________________________")
print()
p = 'Pinjam jam'
b = 'Dikembalikan jam'
print("Masukkan waktu peminjaman. Jam dan menit terpisah")
Pjam = int(input("Jam: "))
if Pjam > 24:
   print("Hanya ada 24 jam")
   exit()
else:
   ()
   
Pmenit = int(input("Menit: "))
if Pmenit >= 60:
   print("Hanya ada 60 menit")
   exit()
else: 
   ()

print("Masukkan waktu pengembalian:")
Bjam = int(input("Jam: "))
if Bjam > 24:
   print("Hanya dapat menyewakan dalam satu hari" )
   exit()
else: 
   ()

Bmenit = int(input("Menit: "))
if Bmenit >= 60:
   print("Hanya ada 60 menit")
   exit()
else:
   ()
print("_______________________________________________________")


print(p, Pjam, ":", Pmenit, b, Bjam, ":", Bmenit)
print()
print()
slsJ = Bjam-Pjam
if slsJ < 0:
   exit("error input")
else:
   ()
slsM = Bmenit-Pmenit
if slsM < 0:
   bm = slsM * -1
else:
   bm = slsM
print("#####################################################")
print("        Waktu peminjaman:",slsJ, "jam", bm, "menit")

if slsJ > 12:
   harga = round(hrg+((slsJ-12)*hrgT)+hrgT*(bm/60))
   h = str(harga)
   print("  Tagihan yang harus dibayar adalah Rp "+h+",00")
elif slsJ <= 12:
   h1 = str(hrg)
   print("  Tagihan yang harus dibayar adalah Rp "+h1+",00")
   
print("######################################################")
print()

byr = int(input("Masukkan nominal pembayaran: "))
print("Anda membayar sebesar Rp", byr, ",-")
if slsJ > 12:
   kmb = byr - harga
   print("Kembaliannya: Rp",kmb)
elif slsJ <= 12:
   kmb1 = byr - hrg
   print("Kembaliannya: Rp",kmb1)
print("==========================================================")
print()

print("Terimakasih sudah memilih jasa kami")
print("Hati-hati di jalan!! ^_^")
