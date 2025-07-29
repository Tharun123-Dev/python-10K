#1generate 5 random floats between 0 and 1
import random
for _ in range(5):
    print(random.random())

#2 dice roll simulator using random.randit
import random
dice=random.randint(1,6)
print(dice)

#3 convert 90 degrees to radians
#radian=degrees*pi/180
import math
degrees=90
radians=math.radians(degrees)
print(radians)

#process2
import math
degrees=90
radians=degrees*math.pi / 180
print(radians)

#4 factorial of agiven number
num=int(input("enter a number: "))
fact=1
while num>1:
    fact=fact*num
    num=num-1
print(fact)

#process2
num=int(input("enter a number: "))
fact=1
for i in range (1,num):
    fact=fact*i
print(fact)

#shuffle a list of 10 integers
import random
list=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(list)
print(list)

#1 lottery draw of 6 unique numbers  from 1 to 49
import random
print(random.sample(range(1,50),6))

#2 Approximate using monte carlo
import random
inside=0
total=10000
for _ in range(total):
    x=random.random()
    y=random.random()

    if x**2+y**2<=1:
        inside+=1
pi=4*inside/total
print(f"approximated pi using monte carlo: {pi}")

#3calculate compound interest using math.pow
#formula A=P(1+r/n)^nt  .....
import math
p=1000 #pricipal amount
r=0.05 # annual interest rate
n=4 # compounded quarterly
t=3 # Time in years
A=p*math.pow(1+r/n,n*t)
print (round (A,2))

#4 Trigonometry calculator using degrees
import math
angle=float(input("enter a number: "))
#conver to radians
rad=math.radians(angle)
#calculate the point
print("sin=", round(math.sin(rad),4))
print("cos=", round(math.cos(rad),4))
print("tan=", round(math.tan(rad),4))

#5 Roll two dice 1000 times and plot the sum frequency
import random
#initailize count dictinary for sums from 2 to 12
freq={i:0 for i in range(2,13)}
#roll two dice 1000 times
for _ in range(1000):
    die1=random.randint(1,6)
    die2=random.randint(1,6)
    total=die1+die2
    freq[total]+=1
#display result
for total in range(2,13):
    print(f"Sum {total}: {freq[total] } times")








