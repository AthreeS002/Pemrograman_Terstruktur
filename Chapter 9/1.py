def ubahHuruf(text, a, b):
    listText = list(text)
    result = ""
    for huruf in listText:
        if (huruf == a):
            huruf = b
        result = ''.join([result, huruf])         

    return result


print(ubahHuruf('MATEMATIKA', 'T', 'S'))


