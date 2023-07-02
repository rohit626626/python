a=5
b=7
c=sum((a,b)) #predefine function
print(c)

#user define function
def fun(x,y):
    print(x+y)
fun(4,5)

#function without variable
def funavg(a,b):
    avg=(a+b)/2
    print(avg)

funavg(a,b)

#function with variable
def funavg(a,b):
    avg=(a+b)/2
    print(avg) #this gien ave

op=funavg(a,b)
print(op) #output is none because no return function use

#function with variable and return function
def funavg(a,b):
    avg=(a+b)/2
    return avg

op=funavg(a,b)
print(op) 

#function with doc string
def funavg(a,b):
    """sum of two number"""
    avg=(a+b)/2
    return avg

op=funavg(a,b)
print(funavg.__doc__) #doc string 
print(op) 

