data = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
        {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chica', 'mid': 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
        {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

print("============================================================")
print("NIM      NAMA MHS           MID     UAS     NA      STATUS")
print("============================================================")


for i in range(len(data)):


    print(data[i]['nim'].ljust(9), end='')
    print(data[i]['nama'].ljust(16), end='')
    print(str(data[i]['mid']).rjust(6), end='')
    print(str(data[i]['uas']).rjust(8))
    
    
    
print("============================================================")
