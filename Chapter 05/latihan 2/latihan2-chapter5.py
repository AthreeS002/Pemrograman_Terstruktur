angka = 0
jumlah = 0

print("Bilangan ganjil dari 0-100")

print()
for i in range(100):
    if (i % 2 == 1):
        print(i, end=' ')
        angka = angka + 1  
print()
print()
print("Banyaknya bilangan ganjil:", angka)
