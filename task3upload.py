#1.check even or odd
num=int(input("enter a number: "))
if num%2==0:
    print(f"{num} is a even number")
else:
    print(f"{num} is a odd number")

#age group clasiifier
age=int(input("given number: ")) 
if (0<age and age<13):
    print("child")
elif(13<=age and  age<20):
    print("teen")
elif(20<=age ):
    print("adult")

#2.check the given number is possitive or  negative or zero
num=float(input('enter a number: '))
if num>0:
    print("it is a possitive number")
elif(num<0):
    print("it is a negative number")
else:
    print("it is a zero")

#3.divisibility checker if a number is divisible by both 3 and 5
num=int(input("enter a number: "))
if num%3==0 and num%5==0:
    print("it is divisible by both 3 and 5")
else:
    print("it is not divisible by both 3 and 5")

#4.findest large two numbers
a=int(input("enter a number: "))
b=int(input("enter a number: "))
if a>b:
    print(f"{a}is larger")
elif b>a:
    print(f" {b} is larger")

else:
    print("both are equal")
#5.traingle validity checker
a=int(input("enter the side1 :"))
b=int(input("enter the side2 :"))
c=int(input("enter the side3 :"))
if(a+b>c or b+c>a or c+a>b):
    print("this sides form a traingle")
else:
    print("this sides cannot form a traingle")