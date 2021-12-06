try:
    nama_file = input("Masukkan nama file: ")
    buka_file = open(nama_file, 'r')
    sandi_caesar = int(input('Masukkan nilai untuk sandi Caesar: '))
    list_text = list(buka_file.readline())

    hasil = ''
    for char_text in list_text:
        if(char_text.isalpha()):
           huruf = ord(char_text)
           huruf_awal = huruf - ord('A')
           baru = (huruf_awal - sandi_caesar) % 26
           sandi_baru = baru + ord('A')
           huruf_baru = chr(sandi_baru)
           hasil += huruf_baru
        else:
           hasil += char_text

    file_akhir = open('hasilFileCaesar.txt', 'w+')
    file_akhir.write(hasil)
    file_akhir.close

except FileNotFoundError:
    print('[File Not Found!]')
