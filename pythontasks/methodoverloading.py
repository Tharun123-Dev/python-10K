# class A:
#     def add (self,a,b):
#         return a+b
#     def add (self,a,b,c):
    
#         return a+b+c
# obj=A()
# print(obj.add(1,2,3))
# print(obj.add(1,2))# it doesn"t take because of latest last one only print


#it is used for printinmg without error
import multipledispatch  
class A:
    @multipledispatch.dispatch(int,int)
    def add (self,a,b):
        return a+b
    @multipledispatch.dispatch(int,int,int)
    def add (self,a,b,c):
      return a+b+c
    @multipledispatch.dispatch(str,str)
    def add (self ,a,b):
       return a+b
obj=A()
print(obj.add(1,2,3))
print(obj.add(1,2))
print(obj.add("nani","tharun"))