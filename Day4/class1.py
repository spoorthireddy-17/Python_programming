class Student():
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f"name of student:{self.name}")
        print(f"rollno:{self.rollno}")
        print(f"marks:{self.marks}")
'''
without constructor
class Student():
  def display(self,name,rollno,marks):
        print(f"name of student:{name}")
        print(f"rollno:{rollno}")
        print(f"marks:{marks}")
here we pass arguments to method display
'''
s1=Student('spoorthi',8,98)
s1.display()
s2=Student('yashwanth',6,99)
s2.display()