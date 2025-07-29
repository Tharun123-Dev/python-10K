
#even numbers using list comprehension
even=[x for x in range(10) if x%2==0]
print(even)

#convert all names in uppercase
names=["tharun","nani","hi","hello"]
op=[x.upper() for x in names]
print(op)

#list of squares of even numbers only
squares=[x*x for x in range(1,10) if x%2==0]
print(squares)


##armstrong numbers using list comprehensions

def armstronnumber(num):
    new=num
 

    new1=num
    count=0
    while new1>0:
      count += 1 
      new1=new1//10


    new2=num
    sum=0
    while new2>0:
      ld=new2%10
      sum+=ld**count
      new2=new2//10
    if new==sum:
       return True
    else:
       return False
    

op=[i for i in range (100,1000) if armstronnumber(i)]
print("Armstrong numbers from 100 to 10000", op)


# ## create a list of perfect squares using list comprehensions
def square(num):
       is_perfect=False
       for x in range(1,num):
              if x*x==num:
                is_perfect=True
                break
       if is_perfect:
            return True
       else:
            return False
result=[x for x in range(1,101) if square(x)]
print(result)

##neon numbers using list comprehensions
def psqy(num):

    square=num**2
    sum=0
    while square>0:
       ld=square%10
       sum+=ld
       square=square//10
    if sum==num:
        return True
    else:
        return False
op=[x for x in range (1,50) if psqy(x)]
print(op)

# # sunny number using list comprehension
def sunny(num):
  i=1
  while i*i<num+1:
     i+=1
  if i*i==num+1:
     return True
  else:
      return False


op=[x for x in range(1,100) if sunny(x)]
print(op)

# ## create a list of sunny using list comprehensions
def sunny(num):
       is_sunny=False
       for x in range(1,num):
              if x*x==num+1:
                is_sunny=True
                break
       if is_sunny:
            return True
       else:
            return False
result=[x for x in range(1,101) if sunny(x)]
print(result)
    
##create a list of revered strings using comprehensions
n=["nani","hai","hello"]
def reverse(i):
  rev=" "
  for x in range(len(i)-1,-1,-1):
    rev+=i[x]
  return rev

op=[  reverse(i)  for i in n]  
# print(op)




def perfect(num):
    is_square=False
    for x in range(0,num):
        if x*x==num:
            is_square=True
    if is_square:
        return True
    else:
        return False
            
op=[x for x in range(0,100) if perfect(x)]
print(op)

def prime(num):
  while(num>1):
     for i in range(2,num):
       if (num%i==0):
          return False
          break
       else:
          return True
    
op=[x for x in range(0,50) if prime(x)]
print(op)


#0
nani=' '
for i in range(0,5):
 nani+=str('*')
 print(nani)


    
  
    
    

 
   
  
  
 

    
 
    
       



