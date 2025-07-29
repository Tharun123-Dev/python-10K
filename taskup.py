#1
x=10
def show():
    x=5
    print(x)#This has local variable so  print x is 5
show()
print(x)#It has a global variable so print x is 10
  #2
def outer():
    x=10

    def inner():
        print(x) #accessing the variable from global function
    inner()
outer()
#3
x="global"
def outer():
    x="outer"
    def inner():
        x="inner"
    inner()
    print("outer:",  x) # it has a global that is outer so outer is printed
outer()
print("global:", x) #same also global varaible have the its printed  global