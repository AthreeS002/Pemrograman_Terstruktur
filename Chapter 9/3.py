def bintang(n):

    ruang = (n*2) - 1
    
    #untuk bagian atas
    for i in range (n//2+1):
       print (('*' * (2*i+1)).center(ruang))
    
    #untuk bagian bawahnya
    for i in range (n//2, 0, -1):
       print (('*' * (2*i-1)).center(ruang))

bintang(7)
