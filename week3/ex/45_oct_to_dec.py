def oct_to_dec(num):
    a = 0
    base = 1
    k = int(num)%10
    if k>=0 and k<=7:
        while (num):
            lastnum = num % 10
            num = int(num / 10)
            a += lastnum * base
            base = base * 8
        return (a)
    else:
        return ("This is not an octal number")
print(oct_to_dec(750))