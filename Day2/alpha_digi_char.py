#to check alphabet digit or special character

def check(ch):
    if('a'<=ch<='z' or 'A'<=ch<='Z'):
        return "alphabet"
    elif('0'<=ch<='9'):
        return "digit"
    else:
        return "special character"
    
ch=input("enter a character:")
res=check(ch)
print(f"{ch} is {res}")