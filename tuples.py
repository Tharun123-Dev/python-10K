days=("sun","mon","tue")
print(days)#print correct
print(type(days))#which type of data structur it is
print(len(days))#size of the tuple
print(days[0])#indexing base
print(days[1][0])#printing m
favdays=("sun",["mon"],"tue")
print(favdays[1][0][1])#printing o 
mixed=("sun",["mon"],"tue",(1,2,3))
mixed=("sun",["mon"],"tue",("nani"))
print(mixed[3][1])
print(mixed[3][2])#for 3 printing
print(len(mixed[3]))#for printing inner tuple lengths also
print (f"size of the tuple is {mixed[3][2]}")#size of the tuple is 3 (in formatig way)

