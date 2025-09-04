#first and last digit of a number

def find(n):
        last=n%10
        while(n>=10):
            n=n//10
        first=n
        print(f"first is {first}, last is {last}")
n=int(input('enter n:'))
find(n)
        