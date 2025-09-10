def addEle(n):
    l=[]
    for i in range(n):
        e=int(input())
        l.append(e)
    return l
def unique(l):
    visited=[]
    l1=[]
    for i in l:
        if(i  not in visited):
            count = 0
            for j in l:
                if i == j:
                    count += 1
            if count==1:
                l1.append(i)       
            visited.append(i)
    return l1
n=int(input("enter no of elements:"))
res=addEle(n)
print(res)
up=unique(res)
print(up)