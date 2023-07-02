#diamond problem
class A:
    def met(self):
        print("This is method of class A")

class B(A):
    def met(self):
        print("This is method of class B")

class C(A):
    def met(self):
        print("This is method of class C")

class D(B,C):
    pass

a=A()
b=B()
c=C()
d=D()

d.met() # d object cerate confusion because d class  inherit class b and c , object d access met(data) class b,c
        # it is diamond problem but python easly sovled this problem //d object first acces first class inherit b
        #class first acces because it first inherit