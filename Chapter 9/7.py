mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
       
print("==========================================================")
print("NIM     NAMA                   TGL LAHIR      TEMPAT")
print("==========================================================")


for data in mhs:
    new_data = data.split(':')
    space = 8
    
    for i in range(len(new_data)):
        if i == 2:
           tgl = new_data[i].split('-')
           tgl.reverse()
           space = 16
           print('/'.join(tgl).ljust(space), end='')
           continue
        print(new_data[i].ljust(space), end='')
        space = 22
    print('')


print("==========================================================")
