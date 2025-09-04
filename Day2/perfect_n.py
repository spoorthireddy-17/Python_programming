#upto n perfect

def display(n):
 
    for num in range(1,n+1):
        s=0
        for i in range(1,(num//2)+1):
            if(num%i==0):
                s=s+i
        if(s==num):
            print(s, end=" ")

n=int(input("enter n:"))
display(n)