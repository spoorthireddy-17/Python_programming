#strong upto n

def check(n):

    for num in range(1,n+1):
        s=0
        r=0
        temp=num
        while(num!=0):
            r=num%10
            f=factorial(r)
            s+=f
            num=num//10
        if(s==temp):
            print(s,end=" ")

def factorial(n):
    i=1
    prod=1
    while(i<=n):
        prod*=i
        i+=1
    return prod

n=int(input('enter n:'))
check(n)
