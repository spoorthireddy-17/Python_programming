def addEle(n):
    l=[]
    for i in range(n):
        e=int(input())
        l.append(e)
    return l
def dup_remove(l):
    unique = []
    for item in l:
        if item not in unique:
            unique.append(item)

    return unique
n=int(input("enter no of elements:"))
res=addEle(n)
print(res)
up=dup_remove(res)
print(up)