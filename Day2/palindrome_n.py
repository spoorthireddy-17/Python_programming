# palindrome upto n

def display(n):
    for num in range(1, n+1):
        s=0
        temp=num
        while(num!=0):
            r=num%10
            s=s*10+r
            num=num//10
        if(s==temp):
            print(s,end=" ")
            
n=int(input('enter n:'))
display(n)