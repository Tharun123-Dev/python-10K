List=["frontend","backend","database",["frontend","backend","database"]]
is_frontend=True
person=int(input("enter ure role in list index: "))
if (is_frontend):
    if person==1:
        print("he is a backend developer")
    elif person==0:
        print("he is a frontend developer")
    elif person==2:
        print("he is a database developer")
    elif person== 3:
        print("he is a fullstack developer")
    else:
        print("learning some tech")
else:
    print("go and join in 1ok coders")




