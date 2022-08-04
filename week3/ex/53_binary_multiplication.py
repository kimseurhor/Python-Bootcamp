def binary_multiplication(num1, num2):
    binnum1 = bin(num1)[2:]
    binnum2 = bin(num2)[2:]
    print('Num1          :', binnum1)
    print('Num2          :', binnum2)
    subbin = bin(int(num1)*int(num2))
    print('Product (Binary) :', subbin[2:])
    print('Product (Decimal) :', num1*num2)

binary_multiplication(60,50)