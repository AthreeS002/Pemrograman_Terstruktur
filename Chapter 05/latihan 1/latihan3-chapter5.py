#memberi variable
s = 'Status Kelulusan                 : ' #s = status

#input nilai
nilai = int(input("Masukkan nilai Bahasa Indonesia  : "))
nilai1 = int(input("Masukkan nilai IPA               : "))
nilai2 = int(input("Masukkan nilai Matematika        : "))

#kesalahan input
if (nilai or nilai1 or nilai2) < 0:
   print()
   print("Maaf, input ada yang tidak valid")
   exit()
elif (nilai or nilai1 or nilai2) > 100:
   print()
   print("Maaf, input ada yang tidak valid")
   exit()

#mulai hitung KKM
elif nilai2 < 70:
   print()
   l = 'TIDAK LULUS' #l = lulus
   print(s+l)
elif (nilai or nilai1) < 60:
   print()
   l = 'TIDAK LULUS'
   print(s+l)
else:
   l = 'LULUS'
   print(s+l)

#jika tidak lulus
if (l == 'TIDAK LULUS'):
   print("Sebab                            : ")
   if nilai < 60:
      print(" - Nilai Bahasa Indonesia kurang dari 60")
   if nilai1 < 60: 
      print(" - Nilai IPA kurang dari 60")
   if nilai2 < 70:
      print(" - Nilai Matematika kurang dari 70")
