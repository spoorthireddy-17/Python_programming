#check armstrong

def check(n):
    s=0
    temp=n
    while(n!=0):
        r=n%10
        s=s+(r*r*r)
        n=n//10
    if(s==temp):
        return 'armstrong'
    else:
        return 'not a armstrong'
    
n=int(input('enter n:'))
res=check(n)
print(f"{n} is {res}")