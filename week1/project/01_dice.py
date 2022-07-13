import random

result =0
print("$ python 01_dice.py")
roll = input("Welcome to the dices game!\nEnter the number of dices you want to roll:")


if roll.isdigit():
    while True:
        if (int(roll) > 8) or (int(roll) < 1):
            print("USAGE: The number must be between 1 and 8")
            roll = input("Enter the number of dices you want to roll:")
        elif int(roll) == 1:
            randomnum = random.randint(1, 6)
            result += randomnum
            print(f"RESULT : {result}")
            break

        elif (int(roll) < 9) and (int(roll) > 1):
            for i in range(1, int(roll) + 1):
                randomnum = random.randint(1, 6)
                print(f"Dice {i} : {randomnum}")
                result += randomnum
            print("="*10)
            print(f"RESULT : {result}")
            print(f"=" * 10)
            break

else:
    while True:
        print("USAGE: The number must be between 1 and 8")
        roll1 = input("Enter the number of dices you want to roll:")
        if roll1.isdigit():
            if (int(roll1) < 9) and (int(roll1) > 1):
                for i in range(1, int(roll1) + 1):
                    randomnum = random.randint(1, 6)
                    print(f"Dice {i} : {randomnum}")
                    result += randomnum
                print(f"="*10)
                print(f"RESULT : {result}")
                print("="*10)
                break
            elif (int(roll1) > 8) or (int(roll1) < 1):
                print("USAGE: The number must be between 1 and 8")
                roll = input("Enter the number of dices you want to roll:")

            elif int(roll1) == 1:
                randomnum = random.randint(1, 6)
                result += randomnum
                print(f"RESULT : {result}")
                break
