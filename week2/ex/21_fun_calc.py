def fun_calc(num1, num2, operator):
    if operator=='+':
        return num1+num2
    elif operator=='-':
        return num1-num2
    elif operator=='*':
        return num1*num2
    elif operator=='/':
        return num1/num2
    else:
        print('Invalid')
print(f"fun_calc(50, 2, '*') product: {fun_calc(50,2,'*')}")
print('Process: 50 * 2=',fun_calc(50,2,'*'))