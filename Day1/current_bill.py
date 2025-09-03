#current bill calculation

num=int(input('enter consumer number:'))
name=input('enter consumer name:')
pmr=float(input('enter present month reading:'))
lmr=float(input('enter last month reading:'))
tu=pmr-lmr
cost=3.80
bill=tu*cost
print('Consumer details:')
print('Consumer number:',num)
print('Consumer name:',name)
print('Present month reading:',pmr)
print('Last month reading:',lmr)
print('Total units:',tu)
print('Current bill:',bill)