class Employes:
    no_of_leaves=25
    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole

    def __add__(self,other): #__add__ is a dunder method
        return self.salary + other.salary

    def __repr__(self): #repr method directly use programer // it print data it call//str and repr both present then str print
        return f"Employes '{self.name}' {self.salary}' '{self.role}'"

    def __str__(self): #str method print string default// str no present, then repr print
        return f"Th ename is {self.name} {self.salary} and {self.role}"


    @classmethod
    def from_dash(cls,string): #class method alternative constructor
        prt=string.split(",")
        return cls(prt[0],prt[1],prt[2])


emp1=Employes("Sumit",8000,"Instructor")
emp2=Employes("Sumit",7000,"Instructor")

nitin=Employes.from_dash("Nitin,9000,manager")

print(emp1+emp2)
print(emp1)
print(repr(emp1))
print(str(emp1))
