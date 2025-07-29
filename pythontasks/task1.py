
#1.check even or odd
num=int(input("enter a number: "))
if num%2==0:
    print("even")
else:
    print("odd")
#2 divisible by 5 but not by 10
num=int(input("enter a number: "))
if num%5==0 and num%10!=0:
    print("It is divisible by 5 not 10")
else:
    print(" condition is not satisfied")

#3 Biggest among two numbers
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print("a is bigger than b That is", a)
else:
    print("b is bigger than a that is ", b)


#using max function alsio
print("the biggest number is: ", max(a,b))
 
 #4 smallest among two numbers
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a<b:
    print("a is smaller  than b That is", a)
else:
    print("b is smaller than a that is ", b)


#using min function alsio
print("the smallest number is: ", min(a,b))


#5.divisible by 2,3 and 6
num=int(input("enter a number: "))
if num%2==0 and num%3==0 and num%6==0:
    print(f"The {num} is divisible by 2,3 and 6")
else:
    print("the condition is not satisfied")
 #process 2

num=int(input("enter a number: "))
if ((num%2==0 and num%3==0) or num%6==0):
    print(f"The {num} is divisible by 2,3 and 6")
else:
    print("the condition is not satisfied")

#6 voting eligibility

age=int(input("enter a number: "))
if age<18:
    print("  not eligible for vote ")
elif(age>=18 and age<110):
    print("eligible for voting ")
else:
    print("rip")

#process 2
age=int(input("enter a number: "))
if age>=18:
    print(" eligible for vote ")
else:
    print(" not eligible for voting ")


#7 student pass/fail based on all subjects >=35

maths=int(input("enter marks (out of 100): "))
physics=int(input("enter marks(out of 100): "))
chemistry=int(input("enter marks (out of 100): "))
if maths>=35 and physics>=35 and chemistry>=35:
    print("pass")
else:
    print("fail")


#8 student pass if passed any one subject (>=35)
maths=int(input("enter marks (out of 100): "))
physics=int(input("enter marks(out of 100): "))
chemistry=int(input("enter marks (out of 100): "))
if maths>=35 or physics>=35 or chemistry>=35:
     print("pass")
else:
     print("fail")

#9  student pass if any two subjects
maths=int(input("enter marks (out of 100): "))
physics=int(input("enter marks(out of 100): "))
chemistry=int(input("enter marks (out of 100): "))
if ((maths>=35 or physics>=35) and chemistry>=35):
    print(" student pass")
elif ((maths>=35 or chemistry>=35) and physics>=35):
    print("student pass")
elif((chemistry>=35 or physics>=35) and maths>=35):
     print("student pass")
else:
    print("fail")




#10 Biggest among three numbers
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
if num1>num2 and num1>num3 :
    print(f"num1 is biggest one ,It is {num1}")
elif num2>num1 and num2>num3:
    print(f"num2 is biggest one, It is {num2}")
else:
    print(f"num3 is biggest one, It is {num3}")

#process 2
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
print(max(num1,num2,num3))

#11 smallest among three numbers
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
if num1<num2 and num1<num3 :
    print(f"num1 is smallest one ,It is {num1}")
elif num2<num1 and num2<num3:
    print(f"num2 is smallest one, It is {num2}")
else:
    print(f"num3 is smallest one, It is {num3}")

    #process 2
num1=int(input("enter a number: "))
num2=int(input("enter a number: "))
num3=int(input("enter a number: "))
print(min (num1,num2,num3))

#12 perfect square or Not
num=int(input("enter a number: "))
found = False 
for x in range(1,num+1):
    if x*x==num:
      print(f"{num} is a perfect square root, square root is {x}")
      found= True
      break
if not found:
    print("not a perfect square number ")

#process 2
num1=int(input("enter a number: "))
a=num1**0.5
print(a)
if a==int(a):
    print("perfect square")
else:
    print("not a perfect square")

    

# 13 cars required for members (max 5 per car)
mem=int(input("enter a members: "))
car_capacity=5
cars_needed=  (mem+car_capacity-1)//5
print(f"Number of the cars required: {cars_needed}")
  
#process 2
mem=int(input("enter a members: "))
if mem%5==0:
    cars=mem//5
else:
    cars=(mem//5)+1
print(cars)


#14 second largest number
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
if (a>b and c>a) or (a>c and b>a):
    print (f"a is the second largest number that is {a}" )
elif (b>a and c>b) or (b>c and a>b):
    print (f"b is the second largest number that is {b}" )
else:
    print (f"c is the second largest number that is {c}" )
    
# using sort method 
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
nums=[a,b,c]
nums.sort()
print(nums[1])

    

#15  leap year or not
year=int(input("enter the  year: "))
if (year % 4==0) and(year % 100!= 0 or year%400==0):
    print(f"the {year} is a leap year")
else:
    print(f"the {year} is not a leap year")