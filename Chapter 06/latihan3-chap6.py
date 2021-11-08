def faktorial(n):
    hitung = 1
    for i in range(1, n+1):
        hitung *= i
    return hitung

def C(a, b):
    return faktorial(a)/faktorial(b)*faktorial(a-b)

def P(a, b):
    return faktorial(a)/faktorial(a-b)

print(int(C(5, 3)))
print(int(P(10, 7)))
