a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9]

a.insert(3, 10)
b.insert(2, 15)
print('a: ', a)
print('b: ', b)

print()

a.append(4)
b.append(8)
print('a: ', a)
print('b: ', b)

print()

a.sort()
b.sort()
print('a: ', a)
print('b: ', b)

print()

c = a[:7]
d = b[2:10]
print('c: ', c)
print('d: ', d)

print()

e = []
if len(c) >= len(d):
    try:
        for i in range(len(c)):
            e += [c[i] + d[i]]
    except IndexError:
        e += [c[i] + 0]
elif len(c) < len(d):
    try:
        for i in range(len(d)):
            e += [c[i] + d[i]]
    except IndexError:
        e += [0 + d[i]]

print('e: ', e)

print()

tuple_e = tuple(e)
print('E_Tuple: ', tuple_e)

print()

print('Nilai minimum dari tuple', tuple_e, 'adalah:', min(tuple_e))
print('Nilai maksimum dari tuple', tuple_e, 'adalah:', max(tuple_e))
print('Jumlah seluruh nilai dari tuple', tuple_e, 'adalah:', sum(tuple_e))

print()

myString = 'python adalah bahasa pemrograman yang menyenangkan'
print(myString)

huruf = set(myString)
print('Huruf penyusunnya:', huruf)

list_huruf = list(huruf)
list_huruf.sort()

print('Diurutkan dari urutan alfabet:', list_huruf)
