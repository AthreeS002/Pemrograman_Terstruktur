mahasiswa = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80}, 
        {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90}, 
        {'nim' : 'A03', 'nama' : 'Chica', 'mid': 100, 'uas' : 50}, 
        {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100}, 
        {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100},
        {'nim' : 'A06', 'nama' : 'Andi', 'mid' : 50, 'uas' : 60}]

print("=================================================================")
print("NIM      NAMA MHS           MID     UAS       NA      STATUS")
print("=================================================================")


for data in mahasiswa:

    NA = (data['mid'] + (2 * data['uas'])) / 3
    data['NA'] = round(NA, 1)
    
    if NA >= 60:
       data['status'] = 'LULUS'
    elif NA < 60:
       data['status'] = 'TIDAK LULUS'

    
    print(data['nim'].ljust(9), end='')
    print(data['nama'].ljust(16), end='')
    print(str(data['mid']).rjust(6), end='')
    print(str(data['uas']).rjust(8), end='')
    print(str(data['NA']).rjust(9), ''.rjust(5), end = '')
    print(data['status'].ljust(7))
    
    
    
print("=================================================================")
