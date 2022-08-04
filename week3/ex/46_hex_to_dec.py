def hex_to_dec(num):
    num=str(num)
    k = set(num)
    kk = {'1','0','2','3','4','5','6','7','8','9','A','B','C','D','E','F'}
    for b in num:
        if b in kk:
            return (int(num,16))

        else:
            return ("This is not a Hex number")

print(hex_to_dec('BA1'))