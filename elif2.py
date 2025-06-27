#conversions
seq=[ "2","4","6","8",]
ip=134252
covert=str(ip)
if(covert[-1] in seq):
    print("even")
else:
    print("odd")


eq=[ 2,4,6,8 ]
ip=134252
covert=str(ip)
if(int(covert[-1] in seq)):
    print("even")
else:
    print("odd")
  # check a person what type skill have and which want to became
person_knows ="backend" 
if(person_knows=="frontened"):
    print("he is a frontend developer")
elif(person_knows=="backend"):
    print("he is a backend developer")
elif(person_knows=="databse"):
    print("he is a database developer")
elif(person_knows==" frontend,backend,database"):
    print("he is a full stack developer")
else:
    print("go and join in 10K ")
