#to check greatest of 3 numbers

def greatest(a,b,c):
    if(a>b):
        if(a>c):
            return f"{a} is greater"
        return f"{c} is greater"
    else:
        if(b>c):
            return f"{b} is greater"
        else:
            return f"{c} is greater"



a=int(input('enter a:'))
b=int(input('enter b:'))
c=int(input('enter c:'))
res=greatest(a,b,c)
print(res)