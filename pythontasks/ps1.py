# # #the even range 1 to 20
# # for i in range(1,21):
# #     if i%2==0:
# #         print(i)
# # # return all the perfect square from 1 to 100
# # for i in range(1,101):
# #     a=i**0.5
# #     if(a==int(a)):
# #         print(i,"it is a perfect square root")
# # for i in range  (1,101):
# #     if( i%2==0):
# #         print( i,"it is n0n prime")

# #     else:
# #         print(i," prime")





# # #problrm solving questions
# #  #1
# # for i in range(5):# In default 0 to start and pr
# #     print(i)
# # #2
# # for i in range(1,21):
# #     if i%2==0:
# #         print(i,"even")
        
# #     else:
# #         print(i,"odd")
# #  #process 2
# # for i in range(1,21):
# #     if i%2==0:
# #         print(i,"even", end="  ")
        
# #     else:
# #         print(i, "odd",end="  ")



# # #3 print the which are is divisible by 5 from 1 to 100
# # for i in range(1,101):
# #     if i%5==0:
# #         print(i,"it is divisible by 5")


# # #count the numbers
# # var=0 
# # for i in range(1,101):
# #     if i%5==0:
# #         var+=1
# #         print(i,"it is divisible by 5")
# # print(var)

# # #4 printing the multiples of 3,multiples of 5 and both from 1 to 50
# # for i in range (1,51):
# #     if (i%3==0 and i%5==0):
# #         print(i, "it is the multiple of 3 and 5")
# #     elif(i%5==0):
# #         print(i,"it is multiple of 5")
# #     elif(i%3==0):
# #         print(i, "it is  multiple of 3")
# #     else:
# #         print("invalid number")

    
# # #5 find the number of numbers is divisible by both 3 and 7 from 1 to 100
# # num=0
# # for i in range(1,101):
# #     if(i%3==0 and i%7==0):
# #         print(i)
# #         num+=1
# # print(num)
# # #6 find the characters in a string is uppercase and lowercase and also count for each one
# # str1=0
# # str2=0
# # str="ThArUnSRikAR"
# # for s in str:
# #     if s.isupper():
# #         print(s,"is upper")
# #         str1+=1

# #     else:
# #         print(s,"is lower")
# #         str2+=1
# # print(str1)
# # print(str2)

# # #perfect square numbers from 1 to 100

# # for i in range(1,101):
# #     root=int(i**0.5)
# #     num=root*root
# #     if num==i:
# #         print(i)

# # #process2
# # for i in range(1,101):
# #     a=i**0.5
# #     if(a==int(a)):
# #         print(i)

# # num=int(input("enter a number: "))
# # b=num**0.5
# # if(b==int(b)):
# #  print(b)
   

# # #check the prime numbers from 1 to 100
# # # for num  in range(1,101):
# # #     if num>1 :
# # #         for x in range(2,num):
# # #             if num%x==0:
# # #                 break
# # #             else:
# # #                 print(num,)


# # for i in range(1,101):
# #     if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0 :
# #         print(i,"prime")
# #     else:
# #         print(i,"nonprime")


# #check the number is prime or not
# num=int(input("enter a number: "))
# if num>1:
#     for i in  range(2,num):
#         if num%i==0:
#             print(num,"not a prime number")
#             break
#     else:
#          print(num, "is a prime number")
# else:
#     print(num, "is not a primr number")



# for i in range(5):
#     if i+1==3:
#           break
#     print("i:",i)
#     print("loope ended")

# s=""
# for i in range(4):
#      if i%2==0:
#           s+="A"
#      else:
#           s+="B"
# print(s)

# a=(3+4)*2**2-5.
# print(a)

# list=[1,2,2,3,1]
# a=set(list)
# print(a)

# set={1,2,2,3,1}
# print(set)

# list=[1,2,2,3,4,5]
# list.remove(2)
# print(list)


# str="abc1234xyz"



# total = sum(int(ch) for ch in str if ch.isdigit())
# print(total)  

# #palindrome

# str="madammadam"
# str1=str[::-1]
# if str==str1:
#      print("true")
# else:
#      print("false")



# str="madammadam"
# str1=str.reverse()
# if str==str1:
#      print("true")
# else:
#      print("false")



list=[23,43,56,76,34]
large=list[0]
sec=list[1]
for i in list:
  

  if large < i:
      sec=large
      large = i
     
  elif sec<i and sec!=large:
        sec=i

print(large)
print(sec)
print(sec)

