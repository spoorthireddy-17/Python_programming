p=int(input('enter principle amount:'))
r=int(input('enter rate of interest:'))
t=int(input('enter time period(months):'))
si=float((p*t*r)/100)
print('simple interest:',si)
total=si+p
print("total amount:",total)