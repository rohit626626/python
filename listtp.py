#list are immutable (changable)
mixed=["mango","copy",45,"tree",10]
print(mixed)
print(mixed[3]) #print lenth 3 (4th pos item) 

num=[1,3,5,6,8,9,7,2]
print(num)
print(min(num)) #print min value
print(max(num)) #print max value
print(len(num)) #print len
print(num[:4]) #sliceing
num.sort() #covert number to asc order
#num.reverse() #covert number to asc order
print(num)

num2=[2,4,5,3,6,8]
num2.append(7) #add item last position
print(num2)

num2=[2,4,5,3,6,8]
num2.insert(2,9) #add item 2nd index
print(num2)

num2=[2,4,5,3,6,8]
num2.pop() #delete last position item
print(num2)

num2=[2,4,5,3,6,8]
num2.remove(3) #delete give item (delete 3 in list)
print(num2)

num2=[2,4,5,3,6,8]
num2[2]=7 #change 2nd index value (1 to 7)
print(num2)


# tuple are mutable (not change)
tp=(1,2,3) #tuple
print(tp)

tp1=(1,) #single value tuple create
print(tp1)

#swapping
a=5
b=6
temp=a
a=b
b=temp
# a,b=b,a #secound method swapping
print(a,b)
