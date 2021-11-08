def sum(*angka):
    hasil = 0
    for data in angka:
       hasil += data
    return hasil

def average(*angka):
    hasil = sum(*angka)
    jumlah = 0
    for data in angka:
        jumlah += 1
    return hasil / jumlah

def max(*angka):
    max = angka[0]
    for data in angka:
        if max < data:
           max = data
    return max

def min(*angka):
    min = angka[0]
    for data in angka:
        if min > data:
           min = data
    return min
