#to check if a number is even or odd

def even_odd(num):
    if(num%2==0):
        return True
    else:
        return False


num=int(input('enter a number:'))
res=even_odd(num)
print(res)