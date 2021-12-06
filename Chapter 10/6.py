try:
    text = 'SAYA SUKA PYTHON'
    sandi_caesar = int(input('Masukkan nilai untuk sandi Caesar: '))
    list_text = list(text)

    hasil = ''
    for char_text in list_text:
        if(char_text.isalpha()):
           huruf = ord(char_text)
           huruf_awal = huruf - ord('A')
           baru = (huruf_awal + sandi_caesar) % 26
           sandi_baru = baru + ord('A')
           huruf_baru = chr(sandi_baru)
           hasil += huruf_baru
        else:
           hasil += char_text

    file_akhir = open('hasilFileCaesar.txt', 'w')
    file_akhir.write(hasil)
    file_akhir.close

except ValueError:
    print("\n[Input Error!]\n")
