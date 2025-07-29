# #call by value

def modify(x):
    x=x+10
    print("change value:",x)
a=5
modify(5)
print("original value:",a)

# #call by reference
def callbyref(listref):
    listref.append(100,200,300)
    print("updatelist:",listref)
originallist=[10,20,30]
callbyref(originallist)
print("originallist:",originallist)