#to check if a number is pos or neg

def pos_neg(num):
    if(num>0):
        return f"{num} is positive"
    else:
        return f"{num} is neagtive"

num=int(input('enter a number:'))
res=pos_neg(num)
print(res)