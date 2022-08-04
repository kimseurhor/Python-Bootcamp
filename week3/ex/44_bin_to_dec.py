def bin_to_dec(num):
    num=str(num)
    k = set(num)
    kk = {'1', '0'}
    if kk==k:
            # or k=={'0'} or k=={'1'}:
        return (int(num,2))
    else:
        return ("This is not a binary number")


print(bin_to_dec("110011"))