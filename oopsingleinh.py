class Employes:
    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole


    @classmethod
    def from_dash(cls,string): #class method alternative constructor
        prt=string.split(",")
        return cls(prt[0],prt[1],prt[2])

class Programmer(Employes): #child class acess parent class method and we add more method in child class
    def __init__(self, ename,esalary, erole,elanguage): #this mathod not good we use super class
        self.name=ename 
        self.salary=esalary
        self.role=erole
        self.language=elanguage #new variable add in child class



sumit=Employes("Sumit",8000,"Instructor")
nitin=Employes.from_dash("Nitin,9000,manager")

sumit=Programmer("Anil",7000,"Teacher","python")

print(sumit.salary)

print(sumit.language)