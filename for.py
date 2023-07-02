#for loop
l1= ["rohan", "mohan", "prince", "nitin"]
print(l1[0], l1[1]) #print only two item

#print all item
for item in l1:
    print(item)

#print all value
l2= [["rohan",3], ["mohan",4], ["prince",2], ["nitin",6]]
for item, age in l2:
    print(item,age)

#convert dict
dic=dict(l2)
print(dic)

#print dic
for item, age in dic.items():
    print(item,age)

#print dic one item
for item in dic:
    print(item)

#quiz //print int number greater 6
items=["rohan",3,5,6,9,7,"naman",8,3]
for item in items:
    if str(item).isnumeric() and item>6:
        print(item)

