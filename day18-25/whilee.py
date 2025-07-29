#sum of the digits
num=1234
sum=0
while(num>0):
    ld=num%10
    sum+=ld
    num=num//10
print(sum)


#squares of sum
num=123
sum=0
while(num>0):
    ld=num%10
    sum+=ld**2
    num=num//10
print(sum)

#find the count using while loop
num=123
count=0
while(num>0):
    ld=num%10
    count+=1
    num=num//10
print(count)


#rev or palindrome
num=1221
num2= num
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)

if num2==rev:
    print("palindrome")
else:
    print("not")


#  #rev or palindrome end with zero
# num=1221
# num2= num
# if(num!)
# rev=0
# while(num>0):
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print(rev)

# if num2==rev:
#     print("palindrome")
# else:
#     print("not")

####amstrong number
num=153
n=num
# step1

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


#reverse of a number
num7=1234
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num7=num7//10
print(rev)
