a = 'LULUS'
b = 'TIDAK LULUS'

nilai = int(input("Masukkan nilai Bhs Indonesia: "))
nilai1 = int(input("Masukkan nilai IPA: "))
nilai2 = int(input("Masukkan nilai Matematika: "))


if nilai2 < 70:
   print("Status Kelulusan: ",b)
   exit()
elif (nilai or nilai1) < 60:
   print("Status Kelulusan: ",b)
   exit()
else:
   ()
print()
print(a)
