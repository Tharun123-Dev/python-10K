# # class Dog:
# #     def __init__(self,name,breed):
# #         self.name=name
# #         self.breed=breed
# #     def bark(self):
# #         print(f"{self.name} is barking")
# # dog1= Dog ("lucky","german shepherd")
# # dog2= Dog("Rocky","beagle")
# # dog3= Dog("charlie","dachshund")
# # dog1.bark()
# # dog2.bark()
# # dog3.bark()

# # #2

# # class Parent:
# #     def __init__ (self,Pname,Pworth):
# #         self.Pname=Pname
# #         self.Pworth=Pworth
# #         print(f"{self.Pname} is the parent")
# #     def passests(self,):
# #         print(f"{self.Pname} assests are {self.Pworth}cr")
# # class ChildActor(Parent):
# #         def __init__(self,Pname,Cname,Pworth):
# #         super().__init__(Pname,Pworth)
# #         self.Cname=Cname
# #         print(f" {self.Cname} is came by the reference of {self.Pname}")
# #     def Cassests(self,worth):
# #         self.Cworth=worth
# #         print(f"{self.Cname} is having worthh of {self.Cworth} cr")
# #     def TotalAssests(self):
# #         print(f"total assests are {self.Cname} is {self.Pworth+self.Cworth}")
# # ramcharan=ChildActor("chiranjeevi","ramcharan",100)
# # ramcharan.Cassests(75)
# # ramcharan.TotalAssests()


       


# class User:
#     def __init__(self,name,email):
#         self.name=name
#         self.email=email

#     def login(self):
#         print(f"{self.name} and also using {self.email}" )

# class Customer(User):
#     def __init__(self,name,email,adress):
#         super().__init__(name,email)
#         self.adress=adress
#     def browse_products(self):
#         print(f"{self.name} to browse products are {self.adress}")
# class Seller(Customer):
#     def __init__ (self,name,email,shop_name):
#         super().__init__(name,email)
#         self.shop_name=shop_name
#     def list_products(self):
#         print(f"browse")


# cust=Customer("nani","nani@gmail.com","mulugu")
# cust.login()
# cust.browse_products()


    















