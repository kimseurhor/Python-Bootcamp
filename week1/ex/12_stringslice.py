a=input("Input a text:")
i=len(a)
if i%2==0:
    str1=a[0:i//2]
    str2=a[i//2:]
else:
    str1=a[0:i//2+1]
    str2=a[i//2+1:]
print(str1+str2)