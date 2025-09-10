def addEle(n):
    l=[]
    for i in range(n):
        e=input()
        l.append(e)
    return l
def freq(l):
    visited=[]
    for i in l:
        if(i  not in visited):
            count = 0
            for j in l:
                if i == j:
                    count += 1
            print(f"{i} occurs {count} times")
            visited.append(i)
n=int(input("enter no of elements:"))
res=addEle(n)
print(res)
freq(res)