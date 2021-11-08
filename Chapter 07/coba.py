try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File tidak ditemukan")
    exit()


print(file.read())
