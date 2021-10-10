import numpy as np
print("========================================================================")
print("                  Menghitung BBM berdasarkan Jarak")
print("========================================================================")
print()
pL = int(input("Konsumsi BBM per liternya dapat mencapai berapa kilometer?: "))
print("Komsumsi BBM : 12Km/Liter")
kps = int(input("Kapasitas maksimum berapa liter?: "))
print("Kapasitas BBM maksimal adalah", kps, "liter")
jrk = int(input( "Jarak Tempuh : "))
bbm = jrk/pL
print("BBM yang dibutuhkan :",bbm, "Liter")
isi = np.ceil(bbm/kps)

print()
print()
print("#############################################")
print(" Banyak Pengisian yang Diperlukan : ", int(isi), "kali")
print("#############################################")
