#factorial of a given number

def fact(n):
    i=1
    prod=1
    while(i<=n):
        prod*=i
        i+=1
    return prod
n=int(input('enter n:'))
res=fact(n)
print(f"fact of {n} is {res}")