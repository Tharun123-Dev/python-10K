# #patterns
# for i in range (1,7):
#     print("*"*i)

# # #2
# # 
# rows=5
# for i in range(1,rows+1):
#     print( " "*(rows-i)+"$"*i)

# #3
# rows=5
# for i in range(1,rows+1):
#     spaces="  "*(rows-i)
#     dollars= " $" * i
#     print(spaces+dollars)

# #4
# rows=5
# for i in range(rows):
#     print(''*i+"*"*(rows-i))

# #5
# rows=5
# for i in range(rows):
#     print(' '*i+"* "*(rows-i))

# #5
# num=1
# rows=4
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num ,end=' ')
#         num+=1
#     print()

# #6
# num=10
# rows=5
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end="  ")
#         num+=1
#     print()

# #7
# rows=5
# for i in range(rows):
#     print(' ' * i,end="")
#     for j in range(rows-i):
#         if j==0 or j==rows-i-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# #8
# rows=5
# for i in range (1,6):
    
# #8
# num=1
# row=5
# for i in range(1,row+1):
#     for j in range(i):
#         print(num ,end=" ")
#         num+=1
#     print()
# #  #9
# num=1
# for i in range (1,5):
#     if i%2==0:
#         end=num+i
#         for j in range(end-1,num-1,-1):
#             print(j,end=" ")
#         num=end
#     else:
#         for  j in range(i):
#             print(num,end=" ")
#             num+=1
#     print()
    
# #10
# start = 1
# for i in range(1, 5):        # 4 lines
#     for j in range(i):       # print i numbers in each line
#         print(start, end="")
#         start += 1
#     if i %2==0:
#         print(start[::-1])
#     print()

#11
# row=5
# for i in range(1,row):
#         print(" "*(row-i)+" *"*i)
# for j in range(row,0,-1):
#         print(" "*(row-j)+" *"*j)
        

# #12
# str="tharunn"
# k=0
# for i in range(1,5):
#     for j in range(i):
#         if k<len(str):
#             print(str[k],end=" ")
#             k+=1
#         else:
#             print("*",end=" ")
#     print()

# #13
# row=6
# for i in range (row-1,0,-1):
#     print (  " "*(row-i)+"* "*i)
# for j in range (2,row):
#     print(" "*(row-j)+"* "*j)

# #10
# num=5
# for i in range(1,num+1):
#     print(" " *(num-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
       
#     print()
# for i in range(num+1,1,-1):
#     print(" " *(num-i),end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
       
#     print()

#11
for i in range ()