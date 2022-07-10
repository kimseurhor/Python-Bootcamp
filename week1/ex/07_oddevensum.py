n = int(input("Input a number:"))
sum = 0
for num in range(0, n + 1, 1):

    if ((num % 2) == 0):
        sum += num
print("Sum of odd numbers: ", sum)
sum=0
for num in range(0, n + 1, 1):

    if ((num % 2) == 1):
        sum += num

print("Sum of even numbers: ", sum)