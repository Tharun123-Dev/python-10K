#f=[1,2,3,4,5,6,7,8,9,]
#for x in f :
 #   print(x)
#tuple
'''t=(1,4,6,8)
print(t*2)
for i in t:
    print(i)
    #for append use convert to list
convert=list(t)
convert.append(9)
print(convert)
#for suppose sum of the two tuples used the map and lambda combination
tuole1=(1,2,3,4,5,)
tuple2=(6,7,8,9,)
res = tuple(map(lambda i,j:i+j, tuole1,tuple2))
print(res)

#list methods
s=[2,3,4,5,7,8,9]
print (s[2 :6])
n=["mango", "banana", "apple", "grapes"]
n.insert(0,"cherry")
print(n)
n=["mango", "banana", "apple", "grapes"]
n.append("cherry")
print(n)
n=["mango", "banana", "apple", "grapes"]
#n.extend["mango","banana", "apple","grapes"]
print(n)
n=["mango", "banana", "apple", "grapes"]
n.remove("banana")
print(n)
n.pop()
print(n)
n.clear() 
print(n)

#dictionary
print("dictionary")


d={1:"nani",2:"tharun",3:"anju"}
print(d[1])
#get
print(d.get(1))
#keys
print(d.keys())
#values
print(d.values())
#items
print(d.items())
d={1:"nani",2:"tharun",3:"anju"}
print(d)
#update
upd=(d.update ({5:"deepu"}))
print(upd)
'''
#for loop in dictionary
d={1:"nani",2:"tharun",3:"anju"}
for i in d:
    print(i)
    # for values
d={1:"nani",2:"tharun",3:"anju"}
for i in d.values():
    print(i)
    #for total items
d={1:"nani",2:"tharun",3:"anju"}
for i in d.items():
    print(i)
    # for length
print(len(d))
#anothe method to create a dictionary
cars=dict(brand="audi",model="q8")
print(cars)