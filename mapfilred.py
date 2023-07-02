#map function 
numbers=["3","4","2","1"]
numbers=list(map(int,numbers)) # map function all string list to change in integer //we are perfome diffrent operation 
                                #for ex add, sub, mul etc
numbers[2]=numbers[2]+1
print(numbers[2])

num=[2,3,1,4]
squ=list(map(lambda x:x*x,num)) #map function all number list generate square
print(squ)

def square(a):
    return a*a

def cube(a):
    return a*a*a

fun=[square,cube]
for i in range(5):
    val=list(map(lambda x:x(i),fun)) # this function print square and cube 5 position (4 index) 
    print(val)

#filter function
l2=[1,4,6,8,9]

def greaternum(num):
    return num>5

ot=list(filter(greaternum,l2)) # filter function filter values, this conditon filter function print greatert value of 5
print(ot)

#reduce function
from functools import reduce

l3=[1,2,3,4]

num1=reduce(lambda x,y:x+y, l3) # reduce function work all item //this condition add all item of list and print output
                               #this condition print l3=10 (1+2+3+4=10) //we perfome different operation (add, mul, sub)
print(num1)
