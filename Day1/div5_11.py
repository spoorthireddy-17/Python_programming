#to check if a number is divisible by 5 and 11 or not

def divisible(num):
    if(num%5==0 and num%11==0):
        return f"{num} is divisible by 5 and 11"
    else:
        return f"{num} is not divisible"

num=int(input('enter a number:'))
res=divisible(num)
print(res)