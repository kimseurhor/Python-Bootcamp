def hex_to_oct(num):

    kk = {'1','0','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}
    for b in num:
        if b in kk:
            return oct(int(num, 16))[2:]
        else:
            return ('This is not a hexa-decimal number')
print(hex_to_oct('2B9'))