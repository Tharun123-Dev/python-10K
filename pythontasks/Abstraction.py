# class A:
#     def method(A):
#         pass
# obj1=A()
# obj1.method()

# #abstract class
# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def method(self):
#         pass
# obj1=A()
# obj1.method() #so abstract class also cant use any object creation

# #concrete method
# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def method(self):
#         pass
#     def method2(self):
#         print("this is a concrete nmethod")
# obj1=A()
# obj1.method()

# #object creation for abstract class by using inheritanced

# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def method1(self):
#         pass
#     def method2(self):
#         print("this is a concrete nmethod")
#     @abstractmethod
#     def method3(self):
#         pass
#     @abstractmethod
#     def method4(self):
#         pass
# class B(A):
#     def method1(self):
#         print("this is a implemented in sub class")
#     def method3(self):
#         print("this is implemented in subclass")
#     def method4(self):
#         print("this is nani") #so we need to same method as a superclass methods
# obj1=B()
# obj1.method1()
# obj1.method2()
# obj1.method3()
# obj1.method4()

#abstract
from abc import ABC, abstractmethod
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def figure(self):
        return "it is a 2_dimensional figure"
class Rectangle(Polygon):
    def sides(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def extramethod(self):
        return "rectangle has 4 sides"
#class use traingle
#class use square 
#etc etc
rect=Rectangle()
rect.sides(10,20)
print(rect.area())
print(rect.perimeter())
print(rect.extramethod())

 