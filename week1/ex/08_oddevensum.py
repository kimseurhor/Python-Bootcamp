n = int(input("Input a number:"))
sum = 0

for num in range(0, n + 1, 1):

    if (not(num % 2) == 0):
        sum=num//2
print("Average of even numbers is: ", sum)
sum = 0
for num in range(0, n + 1, 1):

    if ((num % 2) == 0):
        sum=num//2
print("Average of odd numbers is: ", sum)