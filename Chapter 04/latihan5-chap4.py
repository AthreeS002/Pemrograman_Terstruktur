import matplotlib.pyplot as plt
plt.figure(figsize=[10, 6])
plt.barh(['Laki-laki', 'Perempuan'], [100, 50], color = 'c')

plt.legend()

plt.xlabel('Jumlah')
plt.ylabel('Gender')

plt.title('Perbandingan Mhs')

#export ke png
#plt.savefig('diagram_MHS.png')

plt.show()
