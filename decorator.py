#print function
def funret(num):
    if num==0:
        return print
    if num==1:
        return sum

a=funret(1)
print(a)


#function inside function
def fun1(msg):
    msg("This is message")

fun1(print) #this function print message


#decorator
def dec(fun):
    def msg():
        print("Important message")
        fun()
    return msg
    
@dec
def newfun():
    print("Hello world")

newfun()