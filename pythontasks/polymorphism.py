
# #1
# def sum(*args):
#     if args:
#         start=type(args[0])()
#         for i in args:
#             start+=i
#         return start
# print(sum(1,2))
# print(sum("nani","heh")) 

# #2
# class A:
#     def fun(self):
#         print("A")
# class B:
#     def fun(self):
#         print("B")

# class C:
#     def fun(self):
#         print("C")
# def poly(obj):
#     obj.fun()

# obj1=A()
# obj2=B()
# obj3=C()
# poly(obj1)
# poly(obj2)
# poly(obj3)

# #3
# class Dog:
#     def speak(self):
#         return "woooff"
# class Cat:
#     def speak(self):
#         return "meow"
# class Tiger:
#     def speak(self):
#         return "roar"
# def animal(animals):
#     print(animals.speak())


# dog=Dog()
# cat=Cat()
# tiger=Tiger()

# animal(dog)
# animal(cat)
# animal(tiger)

#4
class SendMsg:
    def send(self,msg):
        print(f"sms sent {msg}")
class SendEmail:
    def send(self,msg):
        print(f"email sent: {msg}")
class Notifier:
    def send(self,msg):
        print(f"notifier sent : {msg}")
def sending(sender,msg):
    sender.send(msg)

sending(SendMsg(),"hi your otp is 2343")
sending(SendEmail(),"hi your netflix is about to expired")
sending(Notifier()," Virus alert!...")
    
    
    