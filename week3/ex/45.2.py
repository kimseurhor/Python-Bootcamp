def bin_to_dec(num):
    num=str(num)
    k = set(num)
    kk = {'0','1','2','3','4','5','6','7'}
    if kk==k:
            # or k=={'0'} or k=={'1'}:
        return (int(num,8))
    # else:
    #     return ("This is not a octal number")


print(bin_to_dec("7"))