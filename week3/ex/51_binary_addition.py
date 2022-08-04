def binary_addition (num1, num2):
    binnum1 = bin(num1)[2:]
    binnum2 = bin(num2)[2:]
    print('Num1          :', binnum1)
    print('Num2          :', binnum2)
    list=[]
    c = '0'
    for i in range(len(binnum1)-1,-1,-1):
        b1 = binnum1[i]
        b2 = binnum2[i]
        if b1=='0' and b2=='0' and c=='0':
            list.append('0')
            c='0'
        elif b1=='1' and b2=='1' and c=='1':
            list.append('1')
            c='1'
        elif (b1=='1' and b2=='0' and c=='0') or (b1=='0' and b2=='1' and c=='0') or (b1=='0' and b2=='0' and c=='1'):
            list.append('1')
            c='0'
        else:
            list.append('0')
            c='1'
    if c=='1':
        list.append('1')
    print('Sum (Binary)  :',"".join(list[::-1]))
    print('Sum (Decimal) :', num1+num2)


binary_addition(60,50)