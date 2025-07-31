
# #1
# class Parent:
#     def method (self):
#         print("parent")
# class Child(Parent):
#     def method (self):
#         print("child")
# obj=Child()
# obj.method()

# #2
# class GrandParent:
#     def method(self):
#         print("grand parent")
# class Parent(GrandParent):
#     def method (self):
#         print("parent")
# class Child(Parent):
#     def method (self):
#         print("child")
# obj=Child()
# obj.method()
# obj.method()
# # obj=Parent()
# # obj.method()

# #multiple
# class Parent1:
#     def method(self):
#         print("parent1")
# class Parent2:
#     def method(self):
#         print("parent2")
# class child(Parent1,Parent2):
#     pass
# obj=child()
# obj.method()  ##because its mro order and pass 
# #is empty then go to mro

# #same name both print uses parentclass.method(self,args)
# class Parent:
#     def method(self):
#         print("this is parent")
# class Child(Parent):
#     def method(self):
#         Parent.method(self)
#         print("this is child")
# c=Child()
# c.method()

# #same name both print uses super().method(args)
# class Parent:
#     def method(self):
#         print("this is parent")
# class Child(Parent):
#     def method(self):
#         super().method()
#         print("this is child")
# c=Child()
# c.method()



##
class vehicle:
    def speed(self):
        print("vehicle speed is normal")
class car(vehicle):
    def speed(self):
        print("car speed is normal")
class cycle(car):
    def speed(self):
        print("cycle speed is normal")

car=car()
cycle=cycle()
car.speed()
