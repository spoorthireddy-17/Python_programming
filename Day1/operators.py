def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b


a=int(input('enter a:'))
b=int(input('enter b:'))
print(f"sum of {a},{b} is:{add(a,b)}")
print(f"difference of {a},{b} is:{sub(a,b)}")
print(f"product of {a},{b} is:{mul(a,b)}")
print(f"division of {a},{b} is:{round(div(a,b),2)}")
print(f"remainder of {a},{b} is:{mod(a,b)}")