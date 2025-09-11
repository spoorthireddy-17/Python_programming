n1=int(input('enter integer1:'))
n2=int(input('enter integer2:'))
try:
    res=n1/n2
    print(res)
except:
    print('zero division error')
finally:
    print('try-except are done')