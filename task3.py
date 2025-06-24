# simple interest formula PTR/100
price=int(input("Enter price: "))
time=int(input("Enter time in months: "))
rate=int(input("Enter rate: "))
simple_interest=(price*time*rate)/100
print(f"simple interest of the given value 10{simple_interest}")
#convert celsius to fahrenheit formula F=(c*9/5)+32
celsius=float(input("Enter value: "))
fahrenheit=((celsius*9/5)+32)
print(f"{celsius} celsius is convert to the  {fahrenheit} in fahrenheit")
#The average of three number
number1=float(input("Enter the first value: "))
number2=float(input("Enter the second value: "))
number3=float(input("Enter the third value: "))
average=((number1+number2+number3)/3)
print(f"Average of three numbers is:{average}")
# area of the circle formula pi*radius*radius then pi=3.14
pivalue= 3.146
radius=float(input("Enter radius: "))
area=(pivalue*radius*radius)
print(f"The area of the circle is:{area}")
#another method
pivalue= 3.146
radius=float(input("Enter radius: "))
area=(pivalue*radius**2)
print(f"The area of the circle is:{area}")

