fruits=["apple","mango","banana"]
print(fruits[0])
print(fruits[2])
print(len(fruits))
fruits[1]="pineapple"
print(fruits)
#updated list is apple pineapple and banana
x=["harish","naresh","suresh","mahesh"]
print(x)
print(id(x))
x[2]="kiran"
print(id(x))
data=[1,2,[4,5],[6,7],8,["something"]]
print(data[2][0])
print(data[3][1])
print(data[5][0][2])
print("something"[2])
mixed=[1,2,"hi",12.5, True]
print(f"value:{mixed[0]}, Type: {type(mixed[0])}")
print(f"value:{mixed[2]}, Type: {type(mixed[2])}")
print(f"value:{mixed[3]},, Type: {type(mixed[3])}")