#to check leap year or not

def leap(yr):
    if(yr%4==0):
        if(yr%100==0 and yr%400==0):
            return f"{yr} is a leap"
        return f"{yr} is  a leap"
    else:
        return f"{yr} is not a leap"
    

year=int(input('enter a year:'))
res=leap(year)
print(res)