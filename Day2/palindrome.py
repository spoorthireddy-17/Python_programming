#palindrome or not

def check(n):
    s=0
    temp=n
    while(n!=0):
        r1=n%10
        s=s*10+r1
        n=n//10
    if(s==temp):
        return 'palindrome'
    else:
        return 'not a palindrome'
    
n=int(input('enter n:'))
res=check(n)
print(f"{n} is {res}")