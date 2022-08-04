def bin_to_hex(num):
    kk = {'1', '0'}
    for b in num:
        if b in kk:
            return hex(int(num, 2))[2:]
        else:
            return ('This is not a binary number')

print(bin_to_hex('11001101'))