#armstrongs upto n


def display(n):
    for num in range(1, n+1):
        temp=num
        s=0
        t=num
        while(t!=0):
            r1=t%10
            s=s+1
            t=t//10
        n1=s
        su=0
        while(num!=0):
            r=num%10
            su=su+pow(r,n1)
            num=num//10
        if(su==temp):
            print(su,end=" ")
            
n=int(input('enter n:'))
display(n)