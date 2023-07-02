def fun(*args): #args function simply add one two and more item //args function use list tuple etc
    print(args)

l=["amit", "sonu","prince"]
fun(*l)

#for loop in args
def fun(*args):
    for item in args: 
        print(item)

l=["amit", "sonu","prince"]
fun(*l)

#args with normal var
def fun(nor,*args): # position are very importantnormal var is first position and args secound position// this is rule
    print(nor)
    print(args)

nor="This is normal variable"
l=["amit", "sonu","prince"]
fun(nor,*l)

#args one element no print
def fun(nor,*args): #nor function no print first element in the list(amit)
    print(args)

l=["amit", "sonu","prince"]
fun(*l)

#normal variable args function with kwargs function
def fun(nor,*args,**kwargs): #position are important //firstly nor, args then kwargs, this is rule
    print(nor)
    for item in args: 
        print(item)
    for key,value in kwargs.items():
        print(key,value)

nor="This is normal function"
l=["amit", "sonu","prince"]
kw={"amit":"mca","sumit":"bca"}
fun(nor,*l,**kw) #this given it position

#normal variable args function with kwargs function and not given function
def fun(nor,*args,**kwargs): #we not pass args kwargs, this function not given error
    print(nor)
nor="This is normal function"
fun(nor) #this given it position
