def xor_operation(num1,num2):
    deci1 = int(num1,16)
    deci2 = int(num2,16)
    print(bin(deci1)[2:])
    print(bin(deci2)[2:])
    print(bin(deci1 ^ deci2)[2:])


xor_operation("33","3D")