try:
    file = open("data.txt", "r")
except FileNotFoundError:
    exit("File tidak ditemukan")


bil1 = int(file.readline())
bil2 = int(file.readline())


try:
    hasil = bil1 / bil2
except ZeroDivisionError:
    exit("Tidak bisa dibagi nol")

print()

try:
    print(bil, "dibagi", bil2, "sama dengan", hasil)
except NameError:
    print("'bil' belum didefinisikan")

