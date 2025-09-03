#KILOMETERS TO MILES  1KM=0.621 MILE

#no argument no return type
'''def km_miles():
    km=int(input('enter kilometer:'))
    miles=0.621*km
    print(f"{km}km in miles is {miles}")

km_miles()'''

#with arguments and no return type
''''def days(d):
    month=(1/30)*d
    year=(1/365)*d
    print(f"{d} days={month} months and {round(year,2)} years")

d=int(input('enter days:'))
days(d)'''

#with arguments and return type
'''def hours(h):
    min=60*h
    return min
h=int(input('enter hours:'))
res=hours(h)
print(f"{h} hour= {res} minutes")'''

#without arguments and with return type
def days():
    hours=int(input('enter hours:'))
    days=(1/24)*hours
    return days

res=days()
print(f"{res} days")