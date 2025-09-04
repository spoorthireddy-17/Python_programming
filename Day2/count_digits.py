#count of digits

def count_digits(n):
    s=0
    r=0
    while(n!=0):
        r=n%10
        s=s+1
        n=n//10
    return s
n=int(input('enter n:'))
res=count_digits(n)
print(f"count of {n} is {res}")