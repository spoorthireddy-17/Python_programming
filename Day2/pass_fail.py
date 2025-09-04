#grades of student

def grade(avg):
    if(m1<40 or m2<40 or m3<40):
        return "Fail"
    else:
        if(81<=avg<=100):
            return "distension"
        elif(71<=avg<80):
            return "A"
        elif(51<=avg<=70):
            return "B"
        elif(41<=avg<=50):
            return "C"
    
m1=int(input('enter subject 1 marks:'))
m2=int(input('enter subject 2 marks:'))
m3=int(input('enter subject 3 marks:'))
total=m1+m2+m3
avg=total/3
res=grade(avg)
print(f"grade {res}")