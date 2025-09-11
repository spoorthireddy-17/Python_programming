class Employee:
    def display(self,name,salary):
        print(f"name of employee:{name}")
        print(f"salary:{salary}")
class Manager(Employee):
    def display(self,name,salary,dept):
        '''print(f"name of employee:{name}")
        print(f"salary:{salary}")'''
        super().display(name,salary)
        print(f"department:{dept}")

e1=Employee()
e1.display('spoorthi',99999)
m1=Manager()
m1.display('spoorthi',989999,'HR')