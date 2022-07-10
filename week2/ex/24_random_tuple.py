import random
def random_tuple(num1):
    kom = []
    pp = 0
    for i in range(1, num1+1):
        b = random.randint(0, 100)
        print(f"Random number{i}: {b}")
        kom.append(b)
        pp += b
    print(tuple(kom))
    print(pp)
random_tuple(5)
