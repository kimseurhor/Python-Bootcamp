a = input("Input your number:")
if a.isdecimal():
    if int(a)%2==0:
        print("The number you have entered is Even")
    else:
        print("The number you have entered is Odd")
else:
    print("Not a valid Number")