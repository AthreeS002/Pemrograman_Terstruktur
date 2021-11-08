#rumus segitiga sama sisi
#a^2 + b^2 = c^2

def segitiga():

    a = int(input("Nilai a: "))
    b = int(input("Nilai b: "))
    c = int(input("Nilai c: "))
    if a**2 + b**2 == c**2:
       return True
    else:
       return False


print(segitiga())
