for x in range(1,11):

    print('2*',x,"=",x*2) #2 table

def mul(num):
    for x in range  (1,11):
        print(f"{num}x {x}= {num*x}")
mul(5)
    
# squares of the number
def squares():
    for x in range(1,11):
        print( f" {x} square is {x*x}")
squares()

#even sqquares and odd cubes

for x in range(1,11):
    if x%2==0:
       print(x**2,"squares")

    else:
        print(x**3,"cubes")
#print numbers from 1 to 20 with specific conditions
#1.if 

for num in range (1,21):
    if(num%2==0 and num%3==0):
        print(num,"fizz buzz")
    elif(num%2==0):
        print(num,"fizz")
    elif(num%3==0):
        print(num,"buzz")
    else:
        print("nani")

# addition of 10 numbers

# def sum_num():
#     for i in range(1,11):
#         sum+=i
#         return sum
# print(sum_num(sum()))
 
# for i in range(1,11):
#     sum += i
# print(sum)

#first 10 numbers total addition
sum=0
for i in range(1,11):
   sum+=i
print(sum)


#function also using this section
def sum():
    add=0
    for i in range(1,11):
        add+=i
    print(f"sum of first 10 number {add}")
sum()
#addition of total numbers squares 

sum=0
for i in range(1,11):
   sum+=i*i
print(sum)

# using functions
def squares():
    add=0
    for x in range (1,11):
        add+=x**2
    print(f"sum of first 10 number squares {add}")
squares()


# range start end step like this
for i in range(2,11,2):
    print(i)
#for suppose give range single digit so printing just repeatable # but in string
for x in range(10):
    print("x")

#multipliction of 5 in functions
def mul (num):
    for x in range(1,11):
     print(f"{num}x{x}={num*x}")
mul(5)

#squares of values
for i in range(1,11):
    print(i**2)
for i in range(1,11):
    print(i*i)

#print even numbers from 1 to 50
for i in range(2,51,2):
         print(i)



    
    