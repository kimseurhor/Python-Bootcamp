a=input("Input a string:")
i=len(a)
if len(a)==0:
    print('String is empty')
if i%2==0:
    str1=a[0:i//2]
    str2=a[i//2:]
else:
    str1=a[0:i//2+1]
    str2=a[i//2+1:]
reverse=str1[::-1]
print(reverse+str2)