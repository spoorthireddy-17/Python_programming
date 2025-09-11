from abc import ABC,abstractmethod
#ABC-abstarct class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,length,breadth):
        a=length*breadth
        print(f"area of rectangle:{a}")
class Circle(Shape):
    def area(self,radius):
        ar=3.14*radius*radius
        print(f"area of circle:{ar}")
        
r1=Rectangle()
r1.area(12,10)
c1=Circle()
c1.area(16)