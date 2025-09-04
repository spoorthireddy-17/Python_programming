#sum of first and last digit of a number

def find(n):
        last=n%10
        while(n>=10):
            n=n//10
        first=n
        sum=first+last
        print(f"sum is {sum}")
n=int(input('enter n:'))
find(n)
        