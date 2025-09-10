def addEle(n):
    l=[]
    ev=0
    o=0
    for i in range(n):
        e=int(input())
        l.append(e)
    for ele in l:
        if(ele%2==0):
            ev+=1
        else:
            o+=1
    print(f"{ev} evens and {o} odds")
n=int(input("enter no of elements:"))
addEle(n)

