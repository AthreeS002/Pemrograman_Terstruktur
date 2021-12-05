def tampilkan_data(data):
    i = 1
    for key, value in data.items():
        print(i, key, ':', value)
        i += 1


def check(data):
    termahal = max(list(data.values()))
    for key, value in data.items():
        if value == termahal:
            return key


buah = {'Apel': 5000,
        'Jeruk': 8500,
        'Mangga': 7800,
        'Duku': 6500}

tampilkan_data(buah)

print('\nBuah termahal adalah', check(buah), ':', buah[check(buah)])
