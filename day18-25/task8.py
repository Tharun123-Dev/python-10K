# #1.add all elements in a list
# list=[1,2,3,4,5]
# sum=0
# for i in list:
#     sum+=i
# print(sum)

# #process2
# list=[1,2,3,4,5]
# total=sum(list)
# print(total)

# # ##2. Find max and min in a list.
# list=[1,2,3,4,5]
# largest=max(list)
# print(largest)

# minimum=min(list)
# # print(minimum)

# #process2
# list=[2,33,44,100,76,89]
# maximum=minimum=list[4]
# for i in list:
#     if i>maximum:
#         maximum=i
# print(maximum)
# for i in list:
#     if i<minimum:
#         minimum=i
# print(minimum)
 
# #3. Count even and odd numbers in a list.
# list=[2,4,6,8,1,3,5,7,9]
# count=0
# count1=0
# for x in list:
#     if x%2==0:
#         count+=1
#     else:
#         count1+=1
# print(count)
# print(count1)

# #4. Reverse a list without using reverse().
# nl=[1,2,3,4,5,6]
# r=[]
# for x in range (len(nl)-1,-1,-1):
#     r.append(nl[x])
# print(r)

# # #5 5. Remove duplicates from list.
# list=[1,3,2,4,5,6,7,3]
# n2=[]
# for i in list:
#     if i not in n2:
#      n2.append(i)
# print(n2)

# # #6. Sort a list of strings by length.
# names=["nani","tharun","hai","hi"]
# names.sort(key=len)
# print(names)

# ##7. Find the second largest number in the list.   
# list=[23,45,67,4,5,87,90,27] 
# large=second=list[3]
# for i in  list:
#     if i>large:
#         second=large
#         large=i
#     elif i>second and i!=large:
#         second=i
# print(second)

# #8. Find sum of all nested list elements.
# nlist=[1,2,[3,4],[5,6],7,8]
# sum=0
# for item in nlist:
#     if type(item)==list:
#         for x in item:
#             sum+=x
#     else:
#      sum+=item
# print(sum)


# #9. Check if two lists are equal.
# list1=[1,3,4,5,6,7]
# list2=[1,3,4,5,6,7]
# if list1==list2:
#     print("both lists are same")
# else:
#     print("not equal")

# #10. Merge two lists and sort them.
# list1=[1,3,5,34,6,7,9]
# list2=[5,6,7,8,4,6]
# list3=list1+list2
# for i in range(len(list3)):
#     for j in range(i+1,len(list3)):
#         if list3[i]>list3[j]:
#             temp=list3[i]
#             list3[i]=list3[j]
#             list3[j]=temp
# print(list3)

# #process2..
# list1=[1,3,5,34,6,7,9]
# list2=[5,6,7,8,4,6]
# list3=list1+list2
# list3.sort()
# print(list3)
# empty=[]
# for i in list3:
#     if i not in empty:
#         empty.append(i)

# print(empty)

# #11. Convert tuple to list and back.
# tuple=(2,4,3,5,6,8,6)
# list1=list(tuple)
# print(list1)

# #and list to tuple
# list1=[2,4,3,5,6,8,6]
# tuple1=tuple(list1)
# print(tuple1)

# #12. Check if the tuple contains a value.
# tuple=(1,2,3,46,76,87,90)
# value=46
# if value in tuple:
#     print( "value contains")
# else:
#     print("not contains")

# #13. Unpack a tuple into variables
# tuple=(2,3,4,5,6,7,23)
# a,b,c,d,e,f,g =tuple
# print("a =",a)
# print("b =",b)
# print("c =",c)
# print("d =",d)
# print("e =",e)
# print("f =",f)
# print("g =",g)

# ##14. Create a list of squares using comprehension.
# squares=[x*x for x in range(1,10)]
# print(squares)

# ## 15. Count how many times a number appears in a list.
# list=[ 1,2,3,1,5,3,4,5,2,1,3]
# number=1
# count=0
# for i in list:
#     if i==number:
#         count+=1
# # print(count)
#  #process2
# list=[ 1,2,3,1,5,3,4,5,2,1,3]
# count=list.count(5)
# print(count)

# #process3.
# list=[ 1,2,3,1,5,3,4,5,2,1,3]
# check=[]

# for num in list:
#     if num not in check:
#         count=0
#         for i in list:
#             if i==num:
#                 count+=1
#         print(f"{num} appears {count} times")
#         check.append(num)

# # #16 16. Find index of element in tuple.
# tuple=(2,3,5,6,34,77)

# index=tuple.index(5)
# print(index)
            
#17. Slice a tuple from index 1 to 3.
tuple=(2,3,5,33,45,23,43)
slice=tuple[1:4]
print(slice)

# #18 18. Replace element in list with another.
list=[2,3,44,54,34,6,5,7,8,87]
list[2]=66
print(list)

#19 19. Filter only strings from mixed lists
list=[2,"nani",3,4,34,"tharun","hai"]
for i in list:
    if i==str(i):
     print(i,"it is a string")

#process2
string=[]
for item in list:
   if type(item)==str:
      string.append(item)
print("string",string)

#20. Take input of the list from the user and print sum.
num= [int(x) for x in input("enter a number separated by space : ").split( )]
print("list =" , num)
sum=0
for i in num:
    sum+=i
print(sum)
 
