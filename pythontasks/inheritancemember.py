
#heirarchy
class Member:
    def __init__(self,firstname,lastname,email,memberid,adress,mobilenumber,datejoined):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.memberid=memberid
        self.adress=adress
        self.mobilenumber=mobilenumber
        self.datejoined=datejoined
    def getfullname(self):
        print(self.firstname+''+self.lastname)
    def changeaddress(self,newaddress):
        self.adress=newaddress
        print("adreesses changed")
    def changenumber(self,newnumber):
        self.mobilenumber=newnumber
        print("mobile number changed")

class Faculty(Member):
    def __init__(self,firstname,lastname,email,memberid,adress,mobilenumber,subjectteaching,salary,datejoined):
       
        self.subjectteaching=subjectteaching
        self.salary=salary
    
        Member.__init__(self,firstname,lastname,email,memberid,adress,mobilenumber,datejoined)
       
    def getsalary(self):
        print("your salary is :",self.salary)

class Student(Member):
    def __init__(self,firstname,lastname,email,memberid,adress,mobilenumber,subjectlearned,gpa,datejoined):
       
        self.subjectlearned=subjectlearned
        self.gpa=gpa
        Member.__init__(self,firstname,lastname,email,memberid,adress,mobilenumber,datejoined)
     
    def getgpa(self):
        print("your gpa is :",self.gpa)

obj=Student("nani","tharun","email","123","hyd","344","eng","10","23/23")
print(obj.firstname)
print(obj.memberid)

#single
# #2

class Parent:
    def __init__ (self,Pname,Pworth):
        self.Pname=Pname
        self.Pworth=Pworth
        print(f"{self.Pname} is the parent")
    def passests(self,):
        print(f"{self.Pname} assests are {self.Pworth}cr")
class ChildActor(Parent):
        def __init__(self,Pname,Cname,Pworth):
         super().__init__(Pname,Pworth)
         self.Cname=Cname
         print(f" {self.Cname} is came by the reference of {self.Pname}")
        def Cassests(self,worth):
         self.Cworth=worth
         print(f"{self.Cname} is having worthh of {self.Cworth} cr")
        def TotalAssests(self):
         print(f"total assests are {self.Cname} is {self.Pworth+self.Cworth}")
ramcharan=ChildActor("chiranjeevi","ramcharan",100)
ramcharan.Cassests(75)
ramcharan.TotalAssests()

#multi-level
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email

    def login(self):
        print(f"{self.name} and also using {self.email}" )

class Customer(User):
    def __init__(self,name,email,adress):
        super().__init__(name,email)
        self.adress=adress
    def browse_products(self):
        print(f"{self.name} to browse products are {self.adress}")
class Seller(Customer):
    def __init__ (self,name,email,shop_name):
        super().__init__(name,email)
        self.shop_name=shop_name
    def list_products(self):
        print(f"browse")


cust=Customer("nani","nani@gmail.com","mulugu")
cust.login()
cust.browse_products()

#muiltiple
class Parent1:
    def P1method(self):
        print("im a p1 method")
class Parent2:
    def P2method(self):
        print("am a parent2")
class child(Parent1,Parent2):
    def Cmethod(self):
        print("am c")
        super().P1method()
        super().P2method()

obj1=child()
obj1.Cmethod()
obj1.P2method()

#hybrid
class A:
    def show(self):
        print("Class A")

class B(A):   # Single inheritance (B -> A)
    def showB(self):
        print("Class B")

class C(A):   # Hierarchical inheritance (C -> A)
    def showC(self):
        print("Class C")

class D(B, C):  # Multiple inheritance (D -> B, C)
    def showD(self):
        print("Class D")

# Object of class D
obj = D()
obj.show()     # From class A
obj.showB()    # From class B
obj.showC()    # From class C
obj.showD()    # From class D

#1
class person():
    def __init__(self,name):
        self.name=name
p=person("john")
print(p.name)

#2
class A:
    def showA(self):
        print("A class")
class B(A):
    def show(self):
        print("B class")
obj=B()
obj.showA()

#3
class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        super().display()
        print("class B")
class C(B):
    def display(self):
        super().display()
        print("class C")

obj=C()
obj.display()

#4
class X:
    def __init__(self):
        print("Init of X")
class Y(X):
    def __init__(self):
        print("Init of Y")
        super().__init__()
class Z(Y):
    def __init__(self):
        print("Init of z")
        super().__init__()
Z=Z()

#5
class Parent:
    name="parent"
class Child(Parent):
    name="Child"

obj=Child()
print(obj.name)

#6
class Base:
    def __init__(self):
        self.value=10
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.value=100
d=Derived()
print(d.value)

#7
class A:
    def __init__(self,a):
        print("class A: ",a)
        
class B(A):
    def __init__(self,a,b):
        super().__init__(a)
        print("class B : ",b)
class C(B):
    def __init__(self, b,a,c):
        super().__init__(a, b)
        print("class C:  ",c)
 

c=C(2,3,1)

# #8
class Person:
     def __init__(self,name):
          self.name=name
class Student(Person):
     def __init__(self,name,roll):
          super().__init__(name)
          self.roll=roll
s=Student("nani",100)
print(s.name)
#print(s.roll)




        



