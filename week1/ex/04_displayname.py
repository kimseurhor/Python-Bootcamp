a = input("Input your name:")
b = int(input("Input number of times to print:"))

if a == "":
    print("No name entered")
else:
    for i in range(b):
        print(a)