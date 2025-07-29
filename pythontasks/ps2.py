# list=["hello","welcome","something","hello","apple","apple"]
# s={}
# for i in list:
#     if i not in s:
#         s[i]=1
#     else:
#         s[i]+=1

# print(s)

# ex="banana"
# d={}
# for i in ex:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)



def prime(num):
    is_prime=True
    for i in range(2,num):
        if num%i==0:
            is_prime==False
            break
    else:
        is_prime=True

prime(11)

#  for i in range(n):

#     for j in range(2,n):
#         if n%i==0:
#             return False
    
#     else:
#         return True
#         count+=1
        
# n=11
# print(is_prime(n))
# print(count)


# count=0
# for i in range(1,10):
   
#     for j in range(2,i):
#         if i%j==0:
            
#             break
#     else:

#         count+=1
# print(count)

# #3
# n1="111"
# n2="100"
# sum=0
# j=0 
# for i in range (len(n1)-1,-1,-1):
#     sum+=int(n1[i])*(2**j)
#     j+=1
# k=0
# for i in range (len(n2)-1,-1,-1):
#     sum+=int(n2[i])*(2**k)
#     k+=1
# print(str(bin(sum)))


# #
# b1="111"
# b2="100"
# sum=bin(int(b1,2)+int(b2,2))
# print(sum)
#
# str="sraaavan"
# for i in str:
#     if 
#         re="a"+i
#     else:
#         print(re+i)  
    
# #consecutive
# s="srcccvan"
# res=s[0]
# c=1
# for i in range(1,len(s)):
#     if s[i]==s[i-1]:
#         c+=1
#         if c<3:
#             res+=s[i]
#     else:
#         c=1
#         res+=s[i]
# print(res)

# #3
# s="sraaavan"
# res=s[0]
# for i in range(1,len(s)):
#     if s[i]!=s[i-1]:
#         res+=s[i]
# print(res)

#4 amout 6 the 1 chocolate price is 1 and then 3 wrwppers sell 1 given choco
A=21
T_c=A
W=A
while W>=3:
    E=W//3
    T_c+=E
    W=E+W%3
print(T_c)



    





