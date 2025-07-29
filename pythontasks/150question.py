# #loop questions
# #1 print all numbers from 1 to 100 cdc
# for i in range(1,101):
#  print(i)


# #2 same but printed in list
# list=[]
# for i in range(1,101):
#  list.append(i)
# print(list)

# #3 write a program to print first n natural numbers and sum
# a=int(input("enter a number: ")) 
# for i in range(1,a+1):
#  print(i)
# sum=i*(i+1)//2
# print(sum)

# #3. print all even numbers from 1 to 50 using while loop
# num=0
# while num<=50:
#     num+=1
#     if num%2==0:
#         print(num,"even")
#     else:
#         print(num,"odd")
        
# #4 write a program to display the multiplication the given number is 20
# for i in range(0,11):
#     print(f" 20*{i}={20*i}")

# # #5. reverse a number using while loop. Also cen we get sum of all the digits
# num=1234
# rev=0
# sum=0
# while num>0:
#     ld=num%10
#     rev=rev*10+ld
#     sum+=ld
#     num=num//10
# print(rev)
# print(sum)

# #6.Write a program to count the digit number of digits in a number using a while loop
# num=23456
# count=0
# while num>0:
#     ld=num%10
#     count+=1
#     num=num//10
# print(count)

# #7.Write a program that keeps asking the user to enter numbers until they enter a negative number. Use a while loop.
# n=int(input("enter a number: "))
# while n>=0:
#      if n>0:
#           print("enter a negative number")
#           break
#      elif n==0:
#          print("enter a negative number")
#          break
     
# else: 
#  print("yes its correct")

# #8.check if a given number is a prime number using a for loop
# num=int(input("enter a number: "))
# for x in range(2,num):
#     if num%x==0:
#       print(num,"not a primr")
#       break
#     else:
#      print(num,"it is a primr")
#      break
# else:
#   print(num,"it is a not prime")
     
# #9.print the 10 terms of the fabonoicci series
# n=int(input("enter a number:"))
# a=0
# b=1
# for i in range(n):
#     print(a)
#     a,b=b,a+b

# #10 write a program to calculate the factorial of a number using a while loop
# nbr = int (input ("Enter a number: "))
# fact=1

# while nbr>0:
#     fact=fact*nbr
#     nbr-=1
# print(fact)

# #using for loop
# n =int(input ("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)
    
# #11 print all nbrs frm 1 to 100 that are divisible by 3 and 5 using a for loop
# for i in range (1,101):  
#     if i%3==0 and i%5==0 :
#         print(i)

# #12 Implement a menu-driven program where the user can choose to
# #find a square nbr find a cube and exit

# while True:
#     print("1.square")
#     print("2.cube")
#     print("3.exit")
#     choice=int(input("enter a number"))
#     if choice==1:
#         n=int(input("enter a number"))
#         print(n*n)
#     elif choice==2:
#         n=int(input("enter a number"))
#         print(n**3)
#     elif choice==3:
      
#         print('exiting')
    
#     else:
#         print("invalid choice")

# #13  implement a basic login system where the user has three attempts to enter the correct password
# correct_pass="nani@123"
# for i in range(3):
#     user_input=input("enter password: ")
#     if user_input==correct_pass:
#         print("login seccessfully")
#         break
#     else:
#         print("wrong one")

# else:
#     print("acess denied")

# #14 reverse a number
# num=12345
# rev=0
# while num>0:
#     ls=num%10
#     rev=rev*10+ls
#     num=num//10
# print(rev)

# #string method
# num=123
# num2=str(num)

# str=''
# for i in  range (len(num2)-1,-1,-1):
#     str+=(num2[i])
# print(str)

# #15 palindrome number
# n=int(input("enter a number: "))
# orig=n
# rev=0
# while n>0:
#     num=n%10
#     rev=rev*10+num
#     n=n//10
# print(rev)
# if orig==rev:
#     print("palindrome")
# else:
#     print("not")

# #16 fabonicci series
# a=0
# b=1
# for i in range(20):
#     print(a)
#     a,b=b,a+b

# # 17 perfect number
# n=int(input("enter a number: "))
# sum=0
# for i in range(1,n):
#     if n%i==0:
#      print(i)
#      sum+=i
# print(sum)
# if sum==n:
#    print("it is perfect number")
# else:
#    print("not")

# #18 Wap to print the Fibonacci series based on user input
# n=int(input("enter a number:"))
# a=0
# b=1
# for i in range (n):
#     print(a)
#     a,b=b,a+b

# # #19 wap to print the non fabonicci numbers by the given input
# n=int(input("enter a number: "))
# a,b=0,1
# fib=[]
# while a<=n:
#     fib.append(a)
#     a,b=b,a+b
# for i in range(n+n):
#     if i not in fib:
#         print(i)

# #20 print 1 to 10 numbers
# for i in range(1,11):
#     print(i)
#p2 
#  i=0
# while i<10:
#     i+=1
#     print(i)

#21 wap to print 10 to 1 without using greater than or less than operator
# for i in range(10,0,-1):
#     print(i)

#p2
#  i=10
# while i>=0:
#     print(i)
#     i-=1

# #22 Wap to print -1 to -10 without using greater than symbol
# for i in range(-1,-11,-1):
#     print(i)
# #p2
# i=-1
# while i!=-11:
    
#     print(i)
#     i-=1

# #23 wap to print sum of digits in a number {input=123 output=6}
# n=1234
# sum=0
# while n>0:
#     ls=n%10
#     sum+=ls
#     n=n//10
# print(sum)

# #process2
# n=input("enter a number: ")
# sum=0
# for i in n:
#     print(i)
#     sum+=int(i)
# print(sum)

# #24 wap to sum of even numbers
# sum=0
# for i in range(1,15):
#     if i%2==0:
#         sum+=i
# print(sum)
#  #in while
# i=1
# sum=0

# while i<11:
#     if i%2==0:
#         sum+=i
#     i+=1
# print(sum)

# #25 wap print whether a given number is a prime or not prime.But need to check 1 also
# n=int(input("enter a number: "))
# if n==1:
#      print("not a prime")

# elif n>1:
#  for x in range(2,n):
        
#         if n%x==0:
#             print("not a prime")
#             break

#  else:
#   print("prime")

# a=not(5>3 and 2<4)
# print(a)

# a="10" +"20" 
# # print(a)
# # 26
# # n = int(input("Enter a number: "))
# def palindrome(n):
#     original = n
#     rev = 0
#     while n != 0:
#         rev = rev * 10 + n % 10
#         n = n // 10

#     if original==rev:
#         print("palin")
#     else:
#         print("not")
# palindrome(121)


# # Main program
# num = int(input("Enter a number: "))
# if is_palindrome(num):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# #27
# def reverse(s):
#     rev = ''
#     for char in s:
#         rev = char + rev
#     print(rev)
# reverse("nani")

# #28 print a prime number upto a given number
# n=int(input("enter a number: "))
# for x in range(2,n+1):
#     for i in range(2,x):
#       if x%i==0:
#          print(x,"not a prime")
#          break
#     else:
#      print( x,"prime")


# #29 print a prime numbers 1 to 100
# for x in range(2,101):
#     for i in range(2,x):
#         if x%i==0:
#             break
#     else:
#         print(x,"primr")

# #30 wap program sum of non primes in a number input3436 output=10
# inp=1234
# sum=0
# while inp>0:
#     ls=inp%10
#     if ls in [2,3,5,7]:
#         sum+=ls
#     inp=inp//10
    
# print(sum)
# #31 wap sum of non prime numbers
# s=2343334
# sum=0
# while s>0:
#     ls=s%10
#     if ls not in [2,3,5,7]:
#         sum+=ls
#     s=s//10
# print(sum)

# #32 wap sum of odd digits in a number
# n=2345674
# sum=0
# while n>0:
#     j=n%10
#     if j%2!=0:
#         sum+=j
#     n=n//10
# print(sum)

# #33 wap sum of even digits in a number
# n=2345674
# sum=0
# while n>0:
#     j=n%10
#     if j%2==0:
#         sum+=j
#     n=n//10
# print(sum)

# #34 wap to check wheather a number is primr or not by using a function
# def prime(n):
#     if n<=1:
#         print("non prime")
#         return
#     for i in range(2,n):
#         if n%i==0:
#             print(n,"It is a non prime")
#             break
#     else:
#         print(n,"primr number")


# prime(8)       
    
# #35 print a prime numbers up to 20
# for i in range(2,21):
#     for x in range(2,i):
#         if i%x==0:
#             #print(i,"not a prime")
#             break
#     else:
#         print(i,"prime")

# #36 armstrong number
# n=153
# new=n

# count=0
# new1=n
# while new1>0:
#     ls=new1%10
#     count+=1
#     new1=new1//10

# new2=n
# sum=0
# while new2>0:
#     ls=new2%10
#     sum+=ls**count
#     new2=new2//10
# if sum==new:
#     print("it is Armstrong")
# else:
#     print("not a Armstrong")

# #37armstrong number with range
# for n in range(1,20):

#  new=n

#  count=0
#  new1=n
#  while new1>0:
#     ls=new1%10
#     count+=1
#     new1=new1//10

#  new2=n
#  sum=0
#  while new2>0:
#     ls=new2%10
#     sum+=ls**count
#     new2=new2//10
#  if sum==new:
#     print(new,"it is Armstrong")
#  else:
#     print(new,"not a Armstrong")

# #38 Wap to check whether minimum is first or maximum is first
# num=input("enter a number")
# min=9
# max=0
# for ch in num:
#     d=int(ch)
#     if d<min:
#         min=d
#     if d>max:
#         max=d
# for ch in num:
#     d=int(ch)
#     if d==min:
#         print("min is first")
#         break
#     elif d==max:
#         print("max is first")
#         break

# #39 WAP a or b is bigger
# a=int(input("enter a number: "))
# b=int(input("enter a number: "))
# if a>b:
#     print("a is bigger")
# else:
#     print("b is bigger")

# #40 a or b or c which is bigger
# a=int(input("enter a number: "))
# b=int(input ("enter a number: "))
# c=int(input("enter a number: "))
# if a>b and a>c:
#     print("a is bigger")
# elif b>c and b>a:
#     print("b is bigger")
# else:
#     print("c is bigger")

# #41 wap to find leap year
# year=int(input("enter a year: "))
# if year%4==0 and (year%100!=0 or year%400==0):
#     print(year,"year is leap year")
# else:
#     print(year,"not a leap year")

# #42 write a program  to find even or odd
# a=int(input("enter a number: "))
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# #43 wap print pass if a student scores more than 40 otherwise not
# marks=int(input("enter a number: "))
# if marks>=40:
#     print("pass")
# else:
#     print("fail")


# #44 vote
# vote=int(input("enter the age: "))
# if vote>=18:
#     print("eligible")
# else:
#     print("not")
       
# #45 wap to check the givemn number is positive,negative or zero
# num=int(input("enter a number: "))
# if num==0:
#     print("it is a zero")
# elif num>0:
#     print("It is positive number")
# elif num<0:
#     print("it is negative number")
# else:
#     print("invalid number")
 
# #46 write a program to display the day of the week based on a number input
# days=["monday","tuesday","wednesday","thursday","friday","saturday"]
# num=int(input("enter a number from 1 to 7: "))
# if 1<=num<=7:
#     print(days[num-1])

# #47 Implement a simple calculator to perform addition,multiplication and division
# a=int(input("enter a number: "))
# operator=(input("enter operator(+,-,*,/,/): "))
# b=int(input("enter a number: "))
# if operator=="+":
#     print("sum is",a+b)
# elif operator=="-":
#     print*("substraction",a-b)
# elif operator=="*":
#     print("multiplication",a*b)
# elif operator=="/":
#     print("division",a/b)
# else:
#     print("invalid input")

# #48dictionary recently asked in review
# x={"name":"nani","age":"30","group":"mca"}
# # print(x)
# # print(x.values())
# # print(x.items())
# # print(x.keys())
# x["name"]="tharun"
# print(x)

# #49 write a program to classify a character entered by the user as a vowel,consonant,or either
# char=input("enter a character(a-z): ")
# if char in ["a","e","i","o","u"]:
#     print("vowel")
# else:
#     print("consonant")

# #50 write a program to check if three sides length from a valid traingle
# a=int(input("enter side 1:"))
# b=int(input("enter side 2:"))
# c=int(input("enter side 3:"))
# if a+b>c and b+c>a and a+c>b :
#     print("valid traingle")
# else:
#     print("not a valid traingle")

# #51 sum of elements in a list
# sum=0
# a=[1,2,3,4,5]
# # print(sum(a))
# for i in a:
#     sum+=i
# print(sum)

#52finding the k Element which is present in a list













# #53 wap to print duplicates digits and unique numbers in a list
# list=[2,3,4,2,4,5,6,7]
# dupli=[]
# unique=[]
# for a in list:
#   if list.count(a)>1:
     
#       if a not in dupli:
#          dupli.append(a)
#   else:
#     unique.append(a)
# print(list)
# print(dupli)
# print(unique)

# #54 Find Unique and Duplicate Digits and if and one digit is duplicated, output: duplicate is x
# #for suppose input=1214 output=2,4 and duplicate is 1

# list=[1,2,1,4]
# d=[]
# u=[]
# for x in list:
#     if list.count(x)>1:
#         if x not in d:
#             d.append(x)
#     else:
#         u.append(x)

# print(list)
# print("duplicate is",d)
# print(u)

# #55
# list=[1,2,3,2,4,5,1,6]
# unique=[]
# duplicates=[]
# for i in list:
#     if i not in unique:
#         unique.append(i)
#     else:
#         if i not in duplicates:
#             duplicates.append(i)
# print(duplicates)

# #56 rev string
# a=121
# st=str(a)
# rev=''
# for i in st:
#     rev=i+rev
# print(rev)
# if rev==st:
#     print("palindrome")
# else:
#     print("not")

## 57count occurences of each digit
# a=2788
# count=[0]*10
# while a>0:
#     s=a%10
#     count[gh]+=1
#     a=a//10
# for i in range(10):
#     if count[i]>0:
#         print(f"{i}",{count[i]})

# #p2
# num=2788
# count={}
# for digit in str(num):
#     if digit in count:
#         count[digit]+=1
#     else:
#         count[digit]=1
# for k in count:
#     print(f"{k}==={count[k]}")
# #p3
# num=2788
# count={}
# while num>0:
#     digit=num%10

#     if digit in count:
#         count[digit]+=1
#     else:
#         count[digit]=1
#     num=num//10
# for k in count:
#     print(f"{k}==={count[k]}")

# #58 wap to check if each number in an list contains duplicate digits ,returning true for duplicates
# #and false for unique digits
# input=[202,89,112,88]

# for i in input:
#     digits=[]
#     temp=i
#     is_duplicate=False
#     while temp>0:
#         digit=temp%10
#         if digit in digits:
#          is_duplicate=True
#          break
#         temp=temp//10
#     print(f"{i}-->{is_duplicate}")

    
# #59sum of each digit in a list
# list=[202,89,112,88]
# for i in list:
#     temp=i
#     sum=0
#     while temp>0:
#         d=temp%10
#         sum+=d
#         temp=temp//10
    
    
#     print(sum)

#60 write a program to check if the digits of each number is an list are in 
# incresing order, returning true or false for each
# # # increasing order or not 
# list=[343,456,213,111]
# for i in list:
#  temp=i
#  is_increasing=True
#  prev_digit=10
#  while temp>0:
#     current_digit=temp%10
#     temp=temp//10

#     if current_digit>=prev_digit:
#           is_increasing=False
#           break
#     prev_digit=current_digit
#  print(is_increasing)

# #61 write a program to check if the digits of each number in 
# # an list are decresing order and return  an list of an true otherwise false
# #decresing order true

# input=[579,111,200,652]
# result=[]
# for i in input:
#     temp=i
#     is_decreasing=True
#     prev_digit=10
#     while temp>0:
#         current_digit= temp%10
#         temp=temp//10

#         if current_digit>=prev_digit:
#          is_decreasing=False
#          break
#         prev_digit=current_digit
#     result.append(is_decreasing)
# print(result)

#62 concate all duplicate numbers in list
# list=[23,33,200,652]
# list2=[]
# for i in list:
#     temp=i
#     digits=[]
#     while temp>0:
#      ds=temp%10
#      if ds in digits and ds not in list2:
#         list2.append(ds)
#      else:
#         digits.append(ds)
#      temp=temp//10
# for i in list2:
#    print(i, end='')

# #63 find the missing number
# list=[34571]
# all=[]
# for x in list:
#     temp=x
#     while temp>0:
#         t=temp%10
    
#         if t not in all:
#             all.append(t)
#         temp=temp//10

    
# for i in range(1,8):
#     if i not in all:
#         print(i)

#64  find largest and smallest numbers in list
# list=[23,12,65,90]
# pre=[]
# for i in list:
#     if i not in pre:
#        pre.append(i)
# for x in pre:
#    if x<i:
#     print(i)
#     break

# #2
# lrg=list[1]
# sml=list[2]
# for i in list:
#     if i>lrg:
#      lrg=i
#     if i<sml:
#      sml=i
# print(lrg)
# print(sml)

#65 find the second and third largest number
# list=[23,43,56,76,34]
# lar=sec=thid=list[2]
# for i in list:
#     if i >lar:
#         thid=sec
#         sec=lar
#         lar=i
#     elif i>sec and i!=lar :
#       thid=sec
#       sec=i
#     elif i>thid and i!=sec and i!=lar:
#        thid=i
         
# print(thid)


# list = [23, 43, 56, 76, 34,44]
# lar = sec = thid = list[0]

# for i in list:
#     if i > lar:
#         thid = sec
#         sec = lar
#         lar = i
#     elif i > sec and i != lar:
#         thid = sec
#         sec = i
#     elif i > thid and i != sec and i != lar:
#         thid = i

# print(thid)
# print(sec)
# print(lar)

# #66 find smallest and second smallest
# list=[27,22,454,66,44,77,12]
# sm=secsm=list[3]
# for i in list:
#     if i<sm:
#         secsm=sm
#         sm=i
#     elif secsm<i and secsm!=sm:
#         secsm=i
# print(secsm)

# #67 reverse an list
# list=[1,2,3,4,5]
# rev=[]
# for char in range(len(list)-1,-1,-1):
#     rev.append(list[char])
# print(rev)

# # 68 Given array of N integer, the task is to replace each element of the array  by its rank in the array
# #    Input: 20 15 26 2 98 6   	Output:4 3   5   1  6 2
# # Explanation: when the array is sorter 2 rank is 1, 6 rank is 2 , 15 rank is 3


# list=[20,15,26,2,98,6]
# rank=[]
# for i in range (len(list)):
#     rank1=1
#     for j  in range (len(list)):
#         if list[i]>list[j]:
#             rank1+=1
#     rank.append(rank1)
# print(rank)




# #69 duplicates and original
# list=[10,30,10,20,10,20,30,10]
# count=0
# list2=[]
# list3=[]
# for  i in list:
#     if i not in list2:
#      list2.append(i)
#     else:
#        list3.append(i)
#        count+=1
# print(list2)
# print(list3)

# #70 finding frequency of an element the list
# list=[10,30,10,20,10,20,30,10]
# checked=[]
# for i in list:
#     if i not in checked:
#         count=0
#         for j in list:
#             if i==j:
#                 count+=1
#         print(i,count)
#         checked.append(i)

# # #71 arrange fir st half is ascending and dsecond half is descending order in a list
# list=[8,7,1,6,5,9]
# n=len(list)
# mid=n//2
# for i in range(mid):
#     for j in range(i+1,mid):
#         if list[i]>list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)
# for i in range(mid,n):
#     for j in range(i+1,n):
#         if list[i]<list[j]:
#             list[i],list[j]=list[j],list[i]
# print(list)

# #72 Given a list of numbers, count the occurences of each number and return a dictionary
# list=[2,3,2,4,5,6,5,4,6,7,7,5,4,3]
# s={}
# for i in list:
#     if i not in s:
#      count=0
#      for j in list:
#         if i==j:
#             count+=1
       
     
#      s[i]=count
# for key, value in s.items():
#    print(key,value)

# #process 2
# def count_occ(numbers):
#     count_dict={}
#     for i in numbers:
#         if i not in count_dict:
#             count_dict[i]=1
#         else:
#             count_dict[i]+=1
#     return count_dict
# nums=[2,3,2,4,5,3,4,6,7,8,8,4,3,2,24,5,667]
# re=count_occ(nums)
# print(re)

#73 Given a list of words,return a dictionary where the keys are words and values are length
#process1
# list=["nani","tharun","naniii","prash"]
# d={}
# for i in list:
#     ds=len(i)
#     d[i]=ds
# print(d)
# #process2
# list=["nani","tharun","naniii","prash"]
# d={}
# for i in list:
#     count=0
#     for j in i:
#      count+=1
#      d[i]=count
# print(d)

# #74 Given a string, return a dictionary where keysb are characters
# #and values their occurances
# str="naniisagoodboy"
# d={}

# for i in str:

#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
    
# print(d)

# #75 given two lists of equal length, create a dictionary where one list
# #contains keys and otherv contain values
# list1=["name","age","course"]
# list2=["tharun","24","mca"]
# #p1
# # dict={}
# # for key,value in zip(list1,list2):

# #     dict[key]=value
# # print(dict)
# #p2
# dict={}
# for i in range(len(list1)):
#     dict[list1[i]]=list2[i]
# print(dict)

# #76swaps keys and values of a dictionary and store keys in a list
# dict={'name': 'tharun', 'age': '24', 'course': 'mca'}
# d2={}
# for key in dict:
#     value=dict[key]
#     d2[value]=key
# keylist=list(d2.keys())

# print(d2)
# print(keylist)

# #78 given a dictionary, find the key with highest value 
# dict={ 'name':35,  'age':32,  'course':9}
# maxk=""
# maxv=0
# for k in dict:
#     if dict[k]>maxv:
#         maxv=dict[k]
#         maxk=k

# print(maxk)

# #79 given a list of numbers,
# # return a dictionary of elements that
# #appear more than once along with thier counts
# list=[1,2,1,2,3,4,4,3,4,5,2]
# s={}
# for i in list:
#     if i not in s:
#         s[i]=1
#     else:
#         s[i]+=1
# print(s)

# #80 given two dictionaries, merge them into one. 
# #if key exists  in both sum their values
# dict1={"namee":2,"age":3,"group":4}
# dict2={"name":5 ,"course":6,"rank":2}
# d={}
# for i in dict1:
#     d[i]=dict1[i]
# for j in dict2:
#     d[j]=dict2[j]

# print(d)

# #81 given two dictionaries, merge them into one. 
# #if key exists  in both sum their values
# dict1={"name":2,"age":3,"group":4}
# dict2={"name":5 ,"course":6,"rank":2}
# d={}
# for i in dict1:
#     d[i]=dict1[i]
# for j in dict2:
#     if j in d:
#      d[j]+=dict2[j]
#     else:
#        d[j]=dict2[j]

# print(d)

# #82 find if 2 strings are anagrams
# # str1="silent"
# # str2="listen"
# # if sorted(str1)==sorted(str2):
# #     print("Anagrams")
# # else:
# #     print("not an anagrams")

# #process2
# str1="silent"
# str2="listen"
# if len(str1)==len(str2):
#     for ch in str1:
#         if str1.count(ch)!=str2.count(ch):
#             print("not")
#             break
#     else:
#             print("anagrams")
# else:
#     print("not anagrams")




# #83 given an algebric equation and remove brackets only
# a="a+((b-c)+d)"
# a=a.replace ("(","")
# a=a.replace (")","")
# print(a)

#guess output
# #1
# a=14
# b=4
# a=a+b
# b=a-b
# print(a,b)

# #2
# x=3
# y=2
# print(x*y//x*y+y-x)

# #3
# sum=0
# for i in range(1,10,2):
#     sum+=i
#     print(sum)

# #4
# x=0
# y=5
# if x+y>20:
#     print("too high")
# elif x-y>20:
#  print("too low")
# else:
#    print("just right")

# #5
# i=1
# while i<10:
#     if i%3==0:
#         print(i,end="")
#     i+=1

# #6
# list=[2,4,6]
# list.append(list[1]*2)
# print(list)

# #7
# for i in range(2):
#     for j in range(2,4):
#         print(i+j,end="")

# #8
# data={"a":1,"b":2,"c":3}
# data["a"]+=data["c"]
# print(data["a"])

# #9
# a=17
# b=5
# print(a%b+a//b)

# #10
# x=True
# y=False
# z=False
# if x or y and z:
#  print("yes")
# else:
#  print("no")

# #11
# for i in range(5):
#     if i==3:
#         break
#     print(i,end="")
# #12
# s={1,2,3}
# s.add(2)
# print(len(s))

# #13
# t=[1,2,[3,4]]
# t[2].append(5)
# print(t)

# #14
# for i in range(3):
#     print(i)
# else:
#     print("loop done")

# #15
# a=False
# b=True
# print(a and b or not a)

# #16
# for i in range(1,4):
#     for j in range(1,i+1):
#         if(i+j)%2==0:
#             print("*",end="")
#         else:
#             print("#,end='")

#     print()

# # 84) Check whether a given string is palindrome or not a palindrome
# # Inp: mom
# # Out: “ palindrome”
# inp="mom"
# str=''
# for i in range(len(inp)-1,-1,-1):
#     str+=inp[i]
# print(str)
# # 85) Check vowels count , consonants count and spaces count in a string
# str="vasjjh ehnjx hsbhbis"
# count=0
# count1=0
# count2=0
# for i in str:
#     if i in ["a","e","i","o","u"]:
#         count+=1
    
#     elif i=='' :
#      count2+=1
#     else:
#         count1+=1
# print(count)
# print(count1)
# print(count2)

#  #86
# for i in range(6):

#         print(i*"*")

# #87
# for i in range(6):
#     for j in range(8,1,-1):
#         print(j*"*")

# #88
# for i in range(6):
#      print(" "*(5-i)+" $ "*i)

# #89
# for i in range(6):
#     print(" "  *(5-i)+"$" *i)

# #90 reverse primitive
# for i in range(6,1,-1):
    
#         print(i*"*")



# #91 sequence of numbers
# num=1
# for i in range(1,5):
#     for j in range(i):
#      print(num,end="")
#      num+=1
#     print()

# #92
# a=True
# b=False
# c=False
# if a or b and c:
#     print("yes")
# else:
#     print("no")

# #93
# for i in range(1,4):
#     for j in range (1,i+1):
#         if (i+j)%2==0:
#             print("*",end="")
#         else:
#             print("#",end=" ")
#     #print()
     
#94 
# a=False
# b=True
# print(a and b or not a)

# s="python"
# for i in range (0,len(s),2):
#     print(s[i]+s[-(i+1)])





















        
    



    




    
           

    













    
        





