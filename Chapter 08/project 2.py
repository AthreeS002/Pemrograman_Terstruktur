def dataStat(x):
    x = tuple(x)
    maksim = max(x)
    minim = min(x)
    average = sum(x) / len(x)

    return [round(average, 2), maksim, minim]


data = [6, 5, 10]
print('Mencari [Rata-rata, Max, Min] dari', data)
print('Yaitu: ', dataStat(data))
