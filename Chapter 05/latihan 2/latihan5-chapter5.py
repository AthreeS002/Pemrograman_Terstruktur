from random import randint

print("Tebak angka dari 0-100")
print()

bil = randint(0, 100)
while True:
   tebak = int(input("Masukkan tebakan anda: "))
   if tebak > bil:
      print("Tebakan anda terlalu besar")
      print()
   elif tebak < bil:
      print("Tebakan anda terlalu kecil")
      print()
   elif tebak == bil:
      print("Selamat, tebakan anda benar")
      break

