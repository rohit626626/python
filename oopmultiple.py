class Employes:
    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole


    @classmethod
    def from_dash(cls,string): #class method alternative constructor
        prt=string.split(",")
        return cls(prt[0],prt[1],prt[2])


class Player:
    def __init__(self, name,game):
        self.name=name
        self.game=game



class Progame(Employes,Player):  
    lan="html"
    def printlan(self):
        print(self.lan)


nitin=Employes.from_dash("Nitin,9000,manager")

amit=Player("Amit","Cricket")
sumit=Progame("Sumit",8000,"Progame")

sumit.printlan()
