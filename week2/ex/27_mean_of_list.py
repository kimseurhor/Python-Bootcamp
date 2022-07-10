def mean_of_list(sum1):
    kimmo = 0
    for i in range(0, len(sum1)):
        kimmo += sum1[i]
        kimmo1 = kimmo/len(sum1)
    print(kimmo1)


print("mean_of_list([50,10,62,32])")
mean_of_list([50,10,62,32])
