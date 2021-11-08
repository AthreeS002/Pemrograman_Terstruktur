nama = input("Masukkan nama File: ")
try:
    file = open(nama, "r")
    print('Isi dari file', nama, 'adalah:\n')
except FileNotFoundError:
    exit("File tidak ditemukan")

print(file.read())
