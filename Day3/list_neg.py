def addEle(n):
    l=[]
    l1=[]
    for i in range(n):
        e=int(input())
        l.append(e)
        if(e<0):
            l1.append(e)
    return l1
n=int(input("enter no of elements:"))
res=addEle(n)
print(res)

