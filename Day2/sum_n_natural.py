#sum of n natural numbers

def add(n):
    i=1
    sum=0
    while(i<=n):
        sum+=i
        i+=1
    return sum
        
n=int(input('enter n:'))
res=add(n)
print(f"sum of {n} natural numbers is {res}")