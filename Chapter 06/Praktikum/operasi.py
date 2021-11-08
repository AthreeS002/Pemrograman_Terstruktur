from operation import *

def satu():
    a = 10
    b = 2
    hasil = jumlah(a, b)
    print('('+str(a), '+', str(b)+')', end = '/')
    return hasil
    
def dua():    
    a = 7
    b = 5
    hasil = jumlah(a, b)
    print('('+str(a),'+',str(b)+')', end = '/')
    return hasil
    
def tiga():    
    a = 12
    b = 34
    hasil = kurang(a, b)
    print('('+str(a),'-',str(b)+')', end = ' = ')
    return hasil

hasil = satu() / dua() / tiga()
print(hasil)


