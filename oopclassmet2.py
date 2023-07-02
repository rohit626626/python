class Employes:
    no_of_leaves=25
    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole


    @classmethod
    def from_dash(cls,string): #class method alternative constructor
        prt=string.split(",")
        return cls(prt[0],prt[1],prt[2])


sumit=Employes("Sumit",8000,"Instructor")
nitin=Employes.from_dash("Nitin,9000,manager")

print(sumit.role)

print(nitin.salary)