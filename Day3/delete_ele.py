def addEle(n):
    l=[]
    for i in range(n):
        e=input()
        l.append(e)
    return l
def delete(pos,l):
    del l[pos]
    return l
n=int(input("enter no of elements:"))
res=addEle(n)
print(res)
pos=int(input('enter position to delete element:'))
updated=delete(pos,res)
print(updated)