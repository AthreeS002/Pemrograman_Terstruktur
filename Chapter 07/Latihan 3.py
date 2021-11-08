nilaiT = 0
hitung = 0

print("-------------------------------------")
print("      PROGRAM HITUNG RATA-RATA")
print("-------------------------------------", '\n')
while True:
	try:
	    nilai = int(input("Masukkan bilangan bulat: "))
	    
	    nilaiT +=nilai
	    hitung = hitung + 1
	    rata2 = nilaiT / hitung
	    
	    lagi = input("Ingin memasukkan lagi? Y/N: ")
	    print()
	    if lagi == 'y' or lagi == 'Y':
	       ()
	    elif lagi == 'n' or lagi == 'N':
	       break
	    else:
	       print("Tolong jawab Y/N saja")
	    
	except ValueError:
	    print("[Bukan bilangan bulat!]", '\n')
	
	
print("Nilai rata-rata nya adalah: ", rata2)
