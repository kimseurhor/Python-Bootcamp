import random
a=random.randint(2000,3000)
c=int(input("Input a number:"))
sum=0
for b in range(0, a+1, 1):
    if((b%2)==0):
        sum=sum+b
print("Sum of even random number:", sum)
