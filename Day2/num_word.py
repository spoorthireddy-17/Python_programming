#convert number to words

def convert(n):
    if(n==0):
        print("zero", end=" ")
    elif(n==1):
        print("one", end=" ")
    elif(n==2):
        print("two", end=" ")
    elif(n==3):
        print("three", end=" ")
    elif(n==4):
        print("four", end=" ")
    elif(n==5):
        print("five", end=" ")
    elif(n==6):
        print("six", end=" ")
    elif(n==7):
        print("seven", end=" ")
    elif(n==8):
        print("eight", end=" ")
    else:
        print("nine", end=" ")
    
n=int(input('enter n:'))
s=0
while(n!=0):
    r1=n%10
    s=s*10+r1
    n=n//10
n1=s
while(s!=0):
    r=s%10
    convert(r)
    s=s//10