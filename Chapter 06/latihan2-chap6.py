def starFunction1(n):
    for i in range (0, n):
        for j in range(0, i+1):
            print("* ", end = "")
        print("\r")
        

def starFunction2(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("* ", end = "")
        print("\r")


def gabung(n):
    starFunction1(n//2)
    if(n % 2 == 0):
       starFunction2(n//2)
    else:
       starFunction2((n//2)+1)


starFunction1(4)
print()
starFunction2(4)
print()
gabung(7)
