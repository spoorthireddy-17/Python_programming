#enter week number and display week name

def week(w):
    if(w==1):
        return "Sunday"
    elif(w==2):
        return "Monday"
    elif(w==3):
        return "Tuesday"
    elif(w==4):
        return "Wednesday"
    elif(w==5):
        return "Thursday"
    elif(w==6):
        return "Friday"
    elif(w==7):
        return "Saturday"
    else:
        return "invalid"
    
n=int(input("enter week number:"))
res=week(n)
print(f"{n} is {res}")