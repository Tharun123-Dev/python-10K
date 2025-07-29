
#     # ipl match tickets available
# tickets_available=True
# if(tickets_available):
#     print("watch  the live  match ipl in the ground")
# else:
#     print("we did not watch")
# tickets_available=not True
# if(tickets_available):
#     print("watch live match ipl in the ground")
# else:
#     print("we did not watch")
# #write a program to check eligibilty of person to vote
# person_age=int(input("enter a number: "))
# if(person_age>18):
#   print("he/she is eligible for vote")
# else:
#   print("he/she is not eligible for vote")
# #check the given number is even or odd
# number=int(input("enter a number: "))
# if(number%2==0):
#    print("It is a even number")
# else:
#    print("It is a odd number")
# if(number%2):
#    print("It is a even number")
# else:
#    print("It is a odd number")
    
    #password strength checker
def check(password_length):
    if password_length>8:
      print("strong password")
    elif password_length>4:
      print(" weak password")
    else:
       print("less password")
check(6)