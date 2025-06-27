def add ():
    a=34
    b=42
    print(a+b)
add()
#parameter and arguements
def add(a,b):  #parameters
    print(a+b)
add(35,36)

#positional arguments

def details(name,pin):
    print(name)
    print(pin)
details(5000,"coders")

#key word arguments
def details(name,pin):
    print(name)
    print(pin)

details(pin=5000, name="coders")

 #default arguements
def details(name,batch=53):
    print(name)
    
   
details("Tharun")
