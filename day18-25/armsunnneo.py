


##armstrong number #it is a number that is equal to the sum of its individual digits where each digit is raised to the power of the digit.

num=153
n=num
# step1##

count=0
new=num
while(new>0):
    ls=n%10
    count+=1  
    new=new//10
     
# #step2
sum=0
new1=num
while(new1>0):
    ls=new1%10
    sum+=ls**count
    new1=new1//10

#comparision
if sum==n:
    print("amstrong number")
else:
    print("not a amstrong number")


# # # armstrong number
num=int(input("enter a number:"))

n=len(str(num))
temp=num
sum=0

while temp>0:
    digit=temp%10
    sum+=digit**n
    temp=temp//10
if sum==num:
    print("armstrong")
else:
    print("not armstrong")






# #neon number #a neon number(9) where the sum of the digit square(9^2=81=8+1) is equal to the original number(9)

num=int(input("enter a number: "))
square=num*num
sum=0
while square>0:
    ls=square%10
    sum+=ls
    square=square//10
if sum==num:
   print(f"{num} is a neon number")
else:
   print(f"{num} is not a neon number")

# #sunny number # A sunny number is a number such that the next number (i.e,number+1) is a perfect square

num=int(input("enter a number: "))
i=1
while i*i<num+1:
    i+=1
if i*i==num+1:
    print(f"{num} is a sunny number")
else:
    print(f"{num} is not a sunny number")


# ##check the number is prime or not
num=int(input("enter a number: "))
if num>1:
    for i in  range(2,num):
        if num%i==0:
            print(num,"not a prime number")
            break
    else:
         print(num, "is a prime number")
else:
    print(num, "is not a primr number")

    

num=int(input("enter a number: "))
if num>1:
    for i in  range(2,num):
        if num%i==0:
            print(num,"not a prime number")
            break
        num=0

    else:
         print(num, "is a prime number")
         
         num+=1
         print(num%i)

     
else:
    print(num, "is not a primr number")

    





