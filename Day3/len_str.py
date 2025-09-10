str1=input('enter string:')
count=0
for s in str1:
    count+=1
print(count)
str2=input('enter second string:')
str=str1+str2
print(str)
#comparing
if(str1==str2):
    print('strings are equal')
elif str1>str2:
    print(f"{str1} is greater")
else:
    print(f"{str2} is greater")