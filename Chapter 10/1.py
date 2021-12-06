myfile = open('text.txt', 'r')

angka = myfile.readlines()

ganjil = 0
genap = 0

for i in range (len(angka)):
    angka[i].replace('\n','')
    hitung = angka[i]
    if (int(hitung) % 2 == 0):
       genap += 1
    else:
       ganjil +=1

print("Banyaknya bilangan ganjil =", ganjil)
print("Banyaknya bilangan genap = ", genap)

