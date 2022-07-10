sum=0
while True:
    a = input("Input a number")
    if a=='stop':
        break
    elif a.isdigit():
        sum+=int(a)
    else:
        print("The input must be a valid number! ")
print(sum)