val1=5
val2=int(input("Enter number: "))
if val2>val1:
    print("greter")
elif val1==val2:
    print("equal")
else:
    print("small")

#list searching
l1=[1,3,5,7,8]
if 5 in l1:
    print("yes")
else:
    print("no")

l2=[1,3,5,7,8]
if 15 not in l2:
    print("yes")
else:
    print("no")