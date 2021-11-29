def bintang(n):
    ruang = (n*2) - 1
    for i in range (n):
       print (('*' * (2*i+1)).center(ruang))

bintang(4)
