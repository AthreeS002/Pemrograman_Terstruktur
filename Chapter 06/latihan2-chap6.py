def bintang1(n):
    for i in range (0, n):
        for j in range(0, i+1):
            print("* ", end = "")
        print("\r")
        

def bintang2(n):
    for i in range(n, -1, -1):
        for j in range(0, i + 1):
            print("* ", end = "")
        print("\r")


def gabung(n):
    bintang1(n//2)
    if(n % 2 == 0):
       bintang2(n//2)
    else:
       bintang2((n//3)+1)


bintang1(4)
print()
bintang2(4)
print()
gabung(7)
