#to check strong

def check(n):
    s=0
    r=0
    temp=n
    while(n!=0):
        r=n%10
        f=factorial(r)
        s+=f
        n=n//10
    if(s==temp):
        print("strong")
    else:
        print("not a strong")
def factorial(n):
    i=1
    prod=1
    while(i<=n):
        prod*=i
        i+=1
    return prod

n=int(input('enter n:'))
check(n)
