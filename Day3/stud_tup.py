students=[]
def stud(n):
    for i in range(n):
        roll=int(input('enter roll no:'))
        name=input('enter name:')
        marks=int(input("enter marks:"))
        student=(roll,name,marks)
        students.append(student)
    for s in students:
        print(i)
    maxi=0
    for s in students:
        if(s[2]>maxi):
            maxi=s[2]
        topper=s
    print(f"{topper[1]} got maximum marks {topper[2]}")
    for s in students:
        if(s[2]>75):
            print(s)
n=int(input('enter number of students:'))
stud(n)