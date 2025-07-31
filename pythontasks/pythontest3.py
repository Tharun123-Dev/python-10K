
# #1
# class person():
#     def __init__(self,name):
#         self.name=name
# p=person("john")
# print(p.name)

# #2
# class A:
#     def showA(self):
#         print("A class")
# class B(A):
#     def show(self):
#         print("B class")
# obj=B()
# obj.showA()

# #3
# class A:
#     def display(self):
#         print("class A")
# class B(A):
#     def display(self):
#         super().display()
#         print("class B")
# class C(B):
#     def display(self):
#         super().display()
#         print("class C")

# obj=C()
# obj.display()

# #4
# class X:
#     def __init__(self):
#         print("Init of X")
# class Y(X):
#     def __init__(self):
#         print("Init of Y")
#         super().__init__()
# class Z(Y):
#     def __init__(self):
#         print("Init of z")
#         super().__init__()
# Z=Z()

# #5
# class Parent:
#     name="parent"
# class Child(Parent):
#     name="Child"

# obj=Child()
# print(obj.name)

# #6
# class Base:
#     def __init__(self):
#         self.value=10
# class Derived(Base):
#     def __init__(self):
#         super().__init__()
#         self.value=100
# d=Derived()
# print(d.value)

# #7
# class A:
#     def __init__(self,a):
#         print("class A: ",a)
        
# class B(A):
#     def __init__(self,a,b):
#         super().__init__(a)
#         print("class B : ",b)
# class C(B):
#     def __init__(self, b,a,c):
#         super().__init__(a, b)
#         print("class C:  ",c)
 

# c=C(2,3,1)

# # #8
# class Person:
#      def __init__(self,name):
#           self.name=name
# class Student(Person):
#      def __init__(self,name,roll):
#           super().__init__(name)
#           self.roll=roll
# s=Student("nani",100)
# print(s.name)
# print(s.roll)
        