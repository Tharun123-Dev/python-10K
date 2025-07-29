# break and continue
for x in range (1,20):
    print(x)
    if x==10:
        break #first will print and then check condition


#example 2
for x in range(1,20):
    if x==10:
        break
    print(x)


#example 3

for x in range (1,20):
    print(x)
    if x==10:
        continue #first will print and then check condition


# #example 4
for x in range(1,20):
      if x==10:
         continue
      print(x)

#example 5
for x in range(1,20):
    if x==6:
      break
    x+=1
    print(x)

#example 6
for x in range(1,20):
    if x==6:
      continue 
    x+=1
    print(x)

#example 4 in list
s=["a","b","c","d","e"]
for i in s:
    if  i=="d":
        break
    print(i)


    #palindromr or not
str="madam" 
op=""
for x in range(len(str)-1,-1,-1):
    
        op+=str[x]
print(op)
if op==str:
     print("palindrome")
else:
    print("palindrome not ")


    
str="madam1"
op=""
while(len(str)-1,-1,-1):
    op+=str
    break
    

print(op)
if op==str:
    print("palindromr")
else:
    print("not")

str="madam"
str1= ""
a=len(str)-1
while a>=0 :
    str1+=str[a]
    a-=1
if str1==str :
    print("palindrome")
    
else:
    print("not palindromr")


# break and continue on list
stops=["srnagar","ameerpet","uppal","barathnagar"]
for stop in stops:
    if stop=="uppal":
        break
    print(stop)


stops=["srnagar","ameerpet","uppal","barathnagar"]
for stop in stops:
    if stop=="uppal":
        continue
    print(stop)

#####while loop
while(True):
    print("nani")
    break
  

#for suppose
list=[2,3,5,6,7,8,89,9]
x=0
while(x<len(list)):
    print(list[x])
    x+=1

# # first 1 to 10 numbers
y=1
while(y<=10):
    print(y)
    y+=1


##it is used in e-commerce like
flashsale=True
while(flashsale):
    print("offers are available")
    break


#even numbers from 1 to 20 
num=2
while(num%2==0 and num<=20):
      print(num)
      num+=2

#odd number from 1 to 20
num=1
while(num<=20):
   print(num)
   num+=2


str="hello"
for x in range(len(str)-1,-1,-1):
    print(str[x],end="")


str="hello"
op=""
for x in range(len(str)-1,-1,-1):
    op+=str[x]
print(op)

    

## task questions and coding 
## check the palindrome in while loop

palin="abdba"
str=""
a=len(palin)-1
while(a>=0):
    str+=palin[a]
    a-=1
if str==palin:
    print("palindrome")
else:
    print("not palindrome")


# in numbers also used this
num=12345
rev=0
while num>0:
   ls=num%10
   rev=rev*10+ls
   num=num//10
print(rev)








