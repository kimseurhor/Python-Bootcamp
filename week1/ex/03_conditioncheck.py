a = int(input("Input your age"))
if a>18:
    print("You are eligible to vote")
elif a<0:
    print("Age must be a positive digit")
else:
    print("You aren't adult yet... Sorry can't vote")