import numpy as np

print("========================================================================")
print("                  Menghitung BBM berdasarkan Jarak")
print("========================================================================")
print()
print()

#jarak
jrkAC = int(input("Berapa kilometer perjalanannya?: "))
print("Jarak dari kota A ke C:", jrkAC, "km")

#bbm = 1 * 12
bbm = int(input("1 Liter BBM dapat mencapai berapa kilometer?: "))
print("BBM:", bbm, "liter per kilometer")
print("Maka BBM yang diperlukan untuk perjalanan:", jrkAC/bbm, "liter")
