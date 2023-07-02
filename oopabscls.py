from abc import ABC, abstractmethod
class Shape(ABC): #abstractbasedclass
    @abstractmethod #abstracmethod is a method it define  inside abstractbasedclass it provide method,function 
                    #and all sub class comploser define method,function for ex- shape class(abstractclass) define function printarea 
                    # rectangle sub class complesor define it function # we not create object in abstractbasedclass
    def printarea(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length=5
        self.breadth=7

    def printarea(self):
        return self.length * self.breadth

rect=Rectangle()
print(rect.printarea())