from random import randint

score = 100
bil = randint(0, 100)

print("Tebak angka mulai dari 0-100")
print()

while True:
   tebak = int(input("Tebakan anda: "))
   if tebak > bil:
      print("Tebakan anda terlalu besar")
      score -= 2
      print()
   elif tebak < bil:
      print("Tebakan anda terlalu kecil")
      score -= 2
      print()
   elif tebak == bil:
      print("Selamat, tebakan anda benar")
      print()
      break
print("Score anda adalah:", score)
