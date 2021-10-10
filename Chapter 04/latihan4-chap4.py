print("=======================================================")
print("              Lama Perjalanan Pak Amir")
print("=======================================================")
print()

def akeb(jrk1, spd):
    return (jrk1)/(spd/60)
def bkec(jrk2, spd1):
    return(jrk2)/(spd1/60)
def ttl(total, total1, rst):
    return (total+total1+rst)

#kota A ke B
jrk1 = float(input("Berapa jarak kilometer dari kota A ke B?: "))
print("Jarak kota A ke kota B adalah", int(jrk1), "kilometer")
spd = float(input("Berapa kecepatan rata-ratanya? (km/jam): "))
print("Kecepatan dari kota A ke kota B sekitar", spd, "km/jam")
total = round(akeb(jrk1, spd))
jam1 = total // 60
menit1 = total % 60
print("Dari kota A ke kota B membutuhkan waktu", total, "menit")
print("Atau sekitar", int(jam1), "jam", menit1,"menit")
print("-------------------------------------------------------")
print()

#kota B ke C
jrk2 = float(input("Berapa jarak dari kota B ke C?: "))
print("Jarak dari kota B ke kota C adalah", int(jrk2), "kilometer")
spd1 = float(input("Berapa kecepatan rata-ratanya?: "))
print("Kecepatan rata-ratanya sekitar", spd1, "km/jam")
total1 = round(bkec(jrk2, spd1))
jam2 = total1 // 60
menit2 = total1 % 60
print("Dari kota B ke kota C membutuhkan waktu", total1, "menit")
print("Atau sekitar", int(jam2), "jam", menit2,"menit")

print("-------------------------------------------------------")
print()

#istirahat
rst = float(input("Berapa menit waktu istirahat?: "))
print("Pak Amir istirahat selama", int(rst), "menit")
ttlo = round(ttl(total, total1, rst))
jam3 = ttlo // 60
menit3 = ttlo % 60
print("total waktu yang dihabiskan adalah", ttlo, "Menit")
print("Atau", jam3, "jam", menit3, "menit")
print()

print("#######################################################")
#jam berangkat
brgkt = int(input("Jam berapa pak Amir berangkatnya?: "))
print("Pak Amir berangkat jam", brgkt)
wktT = (brgkt*60)+ttlo
wkTj = wktT // 60
wkTm = wktT % 60
print("Pak Amir menghabiskan", wktT, "menit selama di perjalanan")
print("Maka perjalan pak Amir dari kota A ke kota C sampai pada jam", wkTj, ":", wkTm)
print("#######################################################")
