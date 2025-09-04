#to check perfect

def check(n):
    s=0
    for i in range(1,(n//2)+1):
        if(n%i==0):
            s=s+i
    if(s==n):
        print("perfect")
    else:
        print("not a perfect")
n=int(input("enter n:"))
check(n)