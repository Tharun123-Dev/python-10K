#1.print each character of the string
# str="hello"
# for char in str:
#  print(char,end=" ")


# #2.sum of the first 10 natural numbers and use for loop with range
# sum=0
# for x in range(1,11):
#   sum=sum+x
# print(f" the first 10 numbers sum is {sum}")
#3.print even numbers from 1 to 20
for y in range (1,21):
  if y%2==0:  
   print(y)
 #4.print elements in a list
list=["pen",'pencil',"eraser"]
for z in list:
    print(z)
#5.print common elements in two lists
lis1=[1,2,3,4,5,6]
lis2=[2,6,7,8,9]
for x in lis1:
        if x in lis2:
            print(x)
# in string
lis1=["banana","apple","mango","grapes"]
lis2=["apple","guava","kiwi","banana"]
for x in lis1:
        if x in lis2:
            print(x)
#6.print all elements in a set
my_set={"apple","banana","cherry"}
for i in my_set:
    print(i)
#7.count how many items are in a set using a loop
colors={"red","blue","green","yellow"}
count=0
for c in colors:
    count+=1
print(f"{count} items are in a set ")

 #8.print all keys and values in a dictionary
person={"name":"alice","age":25,"city":"delhi"}
for key in person:
    print("key:",key, "value:",person[key])

# #
person={"name":"alice","age":25,"city":"delhi"}
for x in person:
    print(x, person[x])

#9 count how many values greater than 50
scores={"math":45,"english":55,"science":80,"history":40}
count=0
for i in scores:
    if scores[i]>50:
        count+=1
print("the scores of greater than 50 is ")
print(count)

 # create a new dictionary with only items where the value is even
data={"a":1,"b":4,"c":6,"d":3}
even_data={}
for i in data:
     if data[i]%2==0:
        even_data[i]=data[i]
print(even_data)







