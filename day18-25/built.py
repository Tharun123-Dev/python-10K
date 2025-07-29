#string length
a="Tharun nani"
count=0
for i in a:
    count+=1
print(count)
print(len(a))#with function 

#number functions
#type coversions
val=10.0
print(int(val)) #doesnt support complex
#float conversion
va=10
print(float(va))
#complex
val=10
val2=20
print(complex(val,val2))
print(complex(val))#taking real only
print(complex(val.real))
print(complex(val.imag))
#absolute
a=10
b=-10
c="nani"
print(abs(a))
print(abs(b))
#print(abs(c))# string not support
#in complex sqrt of a square + b sauare formula
d=3+4j
print(abs(d))
#power
x=2
y=4
print(pow(x,y))
#divmod
a=20
b=10
print(divmod(a,b))# gives the output is quotient and reminder 
##round
print(round(7.5))#even side
print(round(8.5))
print(round(3.1435,3))#3 numbers after point values
print(round(2.52426))
#min and max
tuple=(2,45,67,34,678,9)
print(max(tuple),min(tuple))




