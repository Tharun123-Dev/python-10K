#star patterns
for i in range(1,6):
    print("*"*i)

#number patterns
for i in range(1,6):
    print(str(i)*i)

#using without str method
for i in range(1,6):
    na=0
    for j in range(i):
        na=na*10+i
    print(na)


#specail number used
for i in range(1,6):
    num=i**2
    print(str(num)*i)

#simply 
nani="abcde" 
nani2=""
for i in nani:

    nani2+=i
     
    print(nani2)
    
#ascii
for x in range(97,102):
    str=""
    for y in range(97,x+1):
        str+=chr(y)
    print(str)


#####
str="something"
op=''
for i in str:
    
    for j in i:
        op+=i
    print(op)

#
str="something"
op=''
for i in str:
    
    for j in i:
        op+=i
        print(op)

#inverted star
for i in range(6,0,-1):
    print("*"*i)

#right angled traingle number
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#abcde
# #abcd
st="abcde"
for i in range(len(st),0,-1):
    str1=''
    for j in range(i):
        str1+=st[j]
    print(str1)



