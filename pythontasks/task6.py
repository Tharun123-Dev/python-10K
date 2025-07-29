# #1convert float to int
# a=4.89
# print(int(a))

# #2convert string to int and multiply by 5
# str="7"
# print(int(str))
# print(int(str)*5)

# #3 convert an integer input to float
# a=int(input("enter a number: "))
# print(float(a))

# #4 convert string to float and add 1
# str="3.145"
# print(float(str)+1)

# #5 create a complex number frpm real and img inputs
# c=3
# d=4
# print(complex(c,d))

# #6 return square of a complex number using complex
# d=complex(2,3) #2+3j
# sqr=d**2 #j^2=-1
# print(sqr)

# # 7Round 6.72849 to 2 decimal place
# r=6.72849
# print(round(r,2))

# #8round user-input float to nearest integer
# a=float(input("enter a number: "))
# print(round(a))

# #9find the min and max
# list=[2,5,1,9,-3,6]
# print(min(list))
# print(max(list))

# #10find the largest of three numbers using max
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# c=int(input("enter a number: "))
# print(max(a,b,c))

# #11 find the alphbettically first name from
# list=["Zara","Bob","Alice"]
# a=list[2]
# b=list[1]
# c=list[0]
# print(a,b,c)

# #2
# print(f" alphabatically first name is {min(list)}")

# # 12find pow
# a=2
# b=3
# print(pow(2,3))

# # 13get base and exponential from user ,return result
# base=float(input("enter a number:"))
# ex=float(input("enter a number:"))
# result=pow(base,ex)
# print(result)

# #14 use pow
# x=2
# y=3
# z=5
# res=pow(x,y)
# print(res%z)

# #process 2
# print(pow(x,y,z))#so it defines x**y%z

# #15 use divmod()
# a=23
# # b=5
# # print(divmod(a,b))#quotient and reminder given

# # 16 wite a fun to return quotient and reminder
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# quotient,reminder=divmod(a,b)
# print(quotient,reminder)

##17.convert a nbr to binmary using repeated divmod(num,2)
num=int(input("enter a number: "))          
binary=" "
while num>0:
   num,rem= divmod(num,2)
   binary=str(rem)+binary
print(binary)
 
#  Example for 10:
# divmod(10, 2) → (5, 0) → binary = "0"
# divmod(5, 2) → (2, 1) → binary = "10"
# divmod(2, 2) → (1, 0) → binary = "010"
# divmod(1, 2) → (0, 1) → binary = "1010"
# Final binary = "1010"

#18. absolute value
a=int(input("enter a number: "))
print(abs(a))

#19.#get absolute diff between two numbers
a=int(input("enter a number: "))
b=int(input("enter a number: "))
print(abs(a-b))

# 20 compute mohattan distance from(x,y) to orgin
#mahattan distance |x+0|=|y+0|==|x|+|y|
x=3
y=3
md=abs(x)+abs(y)
print("mahattan distance from orgin:", md)

#21 multiply two strings inputs as integer
a=input("enter a number: ")
b=input("enter a number: ")
result=int(a)+int(b)
print(result)

#22 round pow(5,3)/7 to 3 decimal points
result=pow(5,3)/7
print(round(result,3))

#23 print largest abs value
b=[-2,-8,3,7]
largest=max(b, key=abs)
print(abs(largest))

#process 2
print(max(abs(-2),abs(-8),abs(3),abs(7)))

#Round user float input ,then use as exponent for 2
i=float(input("enter a number: "))
roun=round(i)
print(2**roun)


