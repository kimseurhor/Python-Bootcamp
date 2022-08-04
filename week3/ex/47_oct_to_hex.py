def oct_to_hex(num):

    kk = {'1', '0', '2', '3', '4', '5', '6', '7'}
    for b in num:
        if b in kk:
            return hex(int(num, 8))[2:].upper()
        else:
            return ('This is not an octal number')
print(oct_to_hex('1271'))
