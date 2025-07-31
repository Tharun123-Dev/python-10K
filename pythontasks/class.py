# # class Person:
# #     name="Tharun"
# #     age="24"
# #     gender="male"
# # obj1=Person()
# # obj2=Person()

# # print(obj1)
# # print(obj2)

# # print(obj1.name)
# # print(obj1.age)
# # print(obj2.name)
# # print(obj2.age)

# # #updating
# # obj1.name="nani"
# # print(obj1.name)#only reflected for this
# # print(obj2.name)# does not reflected to object 2
# # print(Person().name)# does not reflect on this

# # #dynamic objects
# # class Socialmedia:
# #     def __init__(x,entertainment,news,sports):
# #         x.enertainment=entertainment
# #         x.news=news
# #         x.sports=sports
# # obj_nani=Socialmedia("Instagram","v6","football")
# # obj_tha=Socialmedia("watsapp","teenmar","Ipl")

# # print(obj_nani.sports)
# # print(obj_tha.sports)


# # ###Socialmedia
# # class Application:
# #     def __init__(app,name,color,purpose):
# #         app.name=name
# #         app.color=color
# #         app.purpose=purpose
    
              
# # insta=Application("instagram","red","social media")
# # youtube=Application("youtube","red","entertainment")
# # zomoto=Application("zomoto","red","food")
# # print(insta.name,insta.color,insta.purpose)
# # print(zomoto.name,zomoto.color,zomoto.purpose)

# # #using dynamic way
# # class Appli:
# #     def __init__(app,name,color):
# #         app.name=name
# #         app.color=color
# #     def purpose(self,app,purpose):
# #         print(f"{app} is used for {purpose}")
# # instagram=Appli("instagram","pink")
# # instagram.purpose("instagram","entertainment")



# # class BankAccount:
# #     def __init__(acc,name,email,ph,balance):
# #         acc.name=name
# #         acc.email=email
# #         acc.ph=ph
# #         acc.balance=balance
# #     def deposit(acc,d_amnt):
# #         acc.balance+=d_amnt
# #     def withdrawl (acc,w_amnt):
# #         acc.balance-=w_amnt
# #     def checkbalance(acc):
# #         print(acc.balance)
# # Tharun_acc=BankAccount("Tharun","nani@gmail.com","6309383826",1000)
# # Tharun_acc.checkbalance()
# # Tharun_acc.deposit(5000)
# # Tharun_acc.withdrawl(2000)
# # Tharun_acc.checkbalance()


# # #static
# # class Apllication:
# #     def __init__(app,name,purpose1,color):
# #         app.name=name
# #         app.purpose1=purpose1
# #         app.color=color
# #     def purpose(self):
# #         print("socaial medai")
# # insta=Apllication("insta","entertainment","pink")
# # print(insta.name,insta.color)
# # insta.purpose()


# #dynamic
# class Apllication:
#     def __init__(app,name,purpose1,color):
#          app.name=name
#          app.purpose1=purpose1
#          app.color=color
#     def purpose(self,app_name,purpose):
#         print(f"{app_name} is used for {purpose}")

# insta=Apllication("insta","enter","pink")
# print(insta.name,insta.purpose1,insta.color)
# insta.purpose("insta","entertainment")


