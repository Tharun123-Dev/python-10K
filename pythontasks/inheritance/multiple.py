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
# obj1.P2method()
count=0
def is_prime(n):
    print("nani")


