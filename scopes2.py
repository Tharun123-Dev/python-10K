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