num=10 #global var
def fun(n):
    #num=5 #local var 
    global num
    num=num+10 # we use global keyword and perform different operation in inside function in global var
    #(for ex use global keyword and change num=10 outside value num+10=20)
    print(num) #print num=5 because num=5 (local var) inside function 
    #// num not in function print function outside(global var) value n=10
    print(n,"number print")
fun("Hello ")
print(num) #print num=10 because num=10 (gloval var) outside function

def outfun():
    x=20
    def infun():
        global x
        x=80
    print("before calling infun",x) #print x value x=20
    infun()
    print("after calling infun",x) #print x value x=20
outfun()
print(x) #print global x value x=80