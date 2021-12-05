def length(x):
    return len(x)


def sortString(list):
    list.sort(key=length, reverse=True)
    return list


myData = ['apel', 'rambutan', 'jeruk']
print('List', myData)
print()
print('Diurutkan berdasarkan jumlah karakter menjadi:')
print(sortString(myData))
