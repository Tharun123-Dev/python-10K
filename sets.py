sets={1,2,3,4}
print(sets)#printing sets
print(type(sets))#type checking
sets={1,2,3,4,4}
print(sets)#does not allow duplicates
#pint(sets[0])does not support index values
normalset={1,23,24,25,25}
normalset.add(26)#adding some value into the set
print(normalset)
normalset.remove(23)
print(normalset)
frozenset=([1,2,3,4,25])
print(frozenset)
print(type(frozenset))
#but the frozen set,it does not support the adding and removing items
#once we created a frozenset, it has locked mode

