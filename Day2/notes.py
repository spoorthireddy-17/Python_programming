#total notes in given amount

def count(amount):
    count=0
    available=[2000,500,200,100,50,20,10,5,2,1]
    for note in available:
        if amount>=note:
            n=amount//note
            print(f"{n}:{note}")
            count+=n
            amount%=note
            
    return count
n=int(input('enter amount:'))
res=count(n)
print(f"{res} number of notes")