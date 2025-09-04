#current bill generation based on units

def calculate(tu):
    if(1<=tu<=50):
        return tu*3.80
    elif(51<=tu<=100):
        return 50*3.80+(tu-50)*4.20
    elif(100<=tu<=200):
        return 50*3.80+50*4.20+(tu-100)*5.10
    elif(200<=tu<=300):
        return 50*3.80+50*4.20+100*5.10+(tu-200)*6.30
    else:
        return  50*3.80+50*4.20+100*5.10+100*6.30+(tu-300)*7.50
    
pmr=float(input('enter present month reading:'))
lmr=float(input('enter last month reading:'))
tu=pmr-lmr
res=calculate(tu)
print(f"bill is {res}")