def check(str):
    alpha=0
    digi=0
    spec=0
    for ch in str:
        if('a'<=ch<='z' or 'A'<=ch<='Z'):
            alpha+=1
        elif('0'<=ch<='9'):
            digi+=1
        else:
            spec+=1
    print(f"{alpha} alphabets, {digi} digits and {spec} special characters")
    
ch=input("enter string:")
check(ch)
