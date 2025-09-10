str=input('enter string:')
pos=[]
find=input('enter the character to search:')
for i in range(len(str)):
    if(str[i]==find):
        pos.append(i)
if(pos):
    print(f"{find} is present at positions {pos}")
else:
    print(f"{find} is not present in {str}")