#1
class Parent:
    def Pmethod(self):
        print("im a method frm parent")
    def Pmethod2(self):
        print("Im a method2 from parent")
class Child(Parent):
    def Cmethod(self):
        print("Im a method from child")
obj1=Child()
obj1.Cmethod()
obj1.Pmethod()
obj1.Pmethod2()

#2
class Parent:
    def Pmethod(self):
        print("im a method frm parent")
    def Pmethod2(self):
        print("Im a method2 from parent")
class Child(Parent):
    def Cmethod(self):
        print("Im a method from child")
        super().Pmethod2()
obj1=Child()
obj1.Cmethod()

#3
class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
class Student(User):
    def __init__(self, name, email,enrollcourse):
        super().__init__(name, email)
        self.enrollcourse=enrollcourse
    def getcourse(self):
        print(f"{self.name} is learning {self.enrollcourse}")
    def removecourse(self,course):
        self.enrollcourse.remove(course)
        self.getcourse()
    def addcourse(self,course):
        self.enrollcourse.append(course)
        self.getcourse()
    

student_obj= Student("nani","nani@gmailcom",["html","css","js"])
student_obj.getcourse()
student_obj.removecourse("html")
student_obj.addcourse("sql")


#4
class Dog:
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
    def bark(nani):
        print(f"{nani.color} and {nani.breed}")
obj1=Dog("brown","husky")
obj2=Dog("red","abroad")
obj1.bark()
obj2.bark()

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


        


