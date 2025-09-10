str=input('enter string:')
pos=[]
find=input('enter the character to search:')
count=0
for i in range(len(str)):
    if(str[i]==find):
        count+=1
if(count>0):
    print(f"{find} present in {str} {count} times")
else:
    print(f"{find} is not present in {str}")