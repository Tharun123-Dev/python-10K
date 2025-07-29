#print("odd")if(num%2!=0)else(print("even"))
op=lambda x: "even"if  x%2==0 else "odd"
print(op(9))
# local global enclosed scopes 
global y
a=20
def glo():
    print(a)
glo()   

#local
def loc():
    a=10
    print(a)
loc()
#enclosed #when use scope values in global
y=50
def en():
  print(y)
  def clo():
         
        y=40
        print(y)

  clo()
en()
op=lambda x : x*x
print(op(5))
#tasks
x="global"
def outer():
    x="outer"
    def inner():
        x="inner"
    inner()
    print("outer:",  x)
outer()
# print("global:", x)
# #2
x=10
def show():
    x=5
    print(x)
show()
print(x)
# #3
def outer():
    x=10

    def inner():
        print(x)
    inner()
0
outer()
def greet():
    msg="hello"
    print(msg) 

greet()

x=2
def show():
    print(x)
show()
count=0
def update():
   global count
   count +=1
   update()
print(count)

def outer():
    x="outer"
    def inner():
        nonlocal x
        x="inner"
    inner()
    print(x)
outer()

 #what happenes if you declare a variablrnwith the same name as a built in fynctiom eg len=[5
#len=5
#print(len("hello")) #so error are there
#possible wihput global declared
x=10
def read():
    print(x)
read()


x=100
def outer():
    x=200
    def inner():
        x=300
        print("inner:", x)
    inner()
    print("outer:", x)
outer()
print("global:", x)


def fun1():
    global x
    x=10


fun1()
print(x)


x=5
def sample():
    x=10
sample()
print(x)


x=5
def sample():
    global x
    x=10
sample()
print(x)




def fumni():
    x=5
    def fun2():
       x=2
    fun2()
    print(x)
fumni()


def fumni():
    x=5
    def fun2():
       nonlocal x
       x=2
    fun2()
    print(x)
fumni()


x="hello"
def fumni():
    x=5
    def fun2():
       nonlocal x
       x=2
    fun2()
    print(x)
fumni()
print(x)












   
