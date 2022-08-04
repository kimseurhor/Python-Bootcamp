# def bin_to_dec(num):
#     num=str(num)
#     k = set(num)
#     kk = {'0','1','2','3','4','5','6','7'}
#     if kk==k:
#             # or k=={'0'} or k=={'1'}:
#         return (int(num,8))
#     # else:
#     #     return ("This is not a octal number")
#
#
# print(bin_to_dec("7"))

# Program to add two matrices using nested loop

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)