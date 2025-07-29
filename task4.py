#even and poostive and even and odd
number=int(input("given number: "))  
if (number>0):
    if (number%2==0):
        print("this is even and posstive")
    else:
        print("this is odd and possitive")
elif(number<0):
    if(number%2==0):
        print("this is even and negative")
    else:
        print("this is odd and negative")
else:

    print("this is zero")


#age group clasiifier
age=int(input("given number: ")) 
if (0<age and age<=12):
    print("kids")
elif(age<=19):
    print("teenage")
elif(age<=40):
    print("young")
elif(age<=59):
    print("prime")
elif(60<age and age<=100):
    print("senior")
else:
    print("rip")



# average grading purpose

s1=int(input("enter marks s1: "))  
s2=int(input("enter marks s2: "))
s3=int(input("enter marks s3: "))  
s4=int(input("enter marks s4: ")) 
s5=int(input("enter marks s5: "))  
s6=int(input("enter marks s6: "))
t=(s1+s2+s3+s4+s5+s6) 
p=(t/600)*100
print(p)
if p>=90:
    print("A grade")
elif p>=80:
    print(" B grade")
elif p>=70:
    print("c grade")
else:
    print("fail")

# traingle checker
a=int(input("enter the side1 :"))
b=int(input("enter the side2 :"))
c=int(input("enter the side3 :"))
if(a+b>c or b+c>a or c+a>b):
    if(a==b==c):
        print("equivalent traingle")
    elif(a==b or b==c or c==a):
        print("isosceles traingle")
    elif(a!=b!=c):
        print("scalene traingle")
else:
    print("this is not a traingle")


#ATm
balance=10000
amount=int(input("enter your withdrawn amout:"))
if(amount<balance):
    if(amount%100==0):
      print( "amount withdrawn succefully")
    else:
      print("ammount enter in multiple of 100's only")
else:
   print("insuficient balance")

#greet no parameters
def greet():
    print("hello tharun")
greet()
# return use
def greet():
    return ("hello nani")
print(greet())
              
#aithematic withe user input perform
def cal(a,b,operator):
 if(operator=="+"): 
  return a+b
 elif(operator=="*"): 
  return a*b 
 elif(operator=="-"): 
  return a-b 
 elif(operator=="/"): 
  return a/b  
 else:
  return "invalid"  
print(cal(1,5,"*"))  


#student and branch
def wish( stu_name="student",branch="engineering"):
    print(f"hello {stu_name} hope u good in {branch}")
student=input("enter student name: ")
branch=input("enter branch name: ")
                      
# wish( student,branch)
def person_age(a,b):
     print(f"hello {a} after 10 years your age is {b+10}")
a=str(input("enter your name: " ))
b=int(input("enter your age: "))
person_age(a,b)


#student
def details(name,pno,adre,email,bg,):
    print(f"your name is {name}")
    print(f"your pno is {pno}")
    print(f"your adre is {adre}")
    print(f"your bg is {bg}")
    print(f"your email{email}")
details(name="tharun",bg="o",adre="venkatapur",pno="630938",email="nani@gmail")
