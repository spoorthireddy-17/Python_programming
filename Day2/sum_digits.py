#sum of digits

def sum_digits(n):
    s=0
    r=0
    while(n!=0):
        r=n%10
        s=s+r
        n=n//10
    return s
n=int(input('enter n:'))
res=sum_digits(n)
print(f"sum of {n} is {res}")