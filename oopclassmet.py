class Employes:
    no_of_leaves=25
    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole

    @classmethod
    def change_leaves(cls,newleaves): #class method change value, we use change value // object are simply change value
        cls.no_of_leaves = newleaves


sumit=Employes("Sumit",8000,"Instructor")
anil=Employes("Anil",3000,"Worker")

print(sumit.salary)
print(anil.role)
sumit.change_leaves(30)
print(sumit.no_of_leaves)
sumit.change_leaves(33)
print(anil.no_of_leaves)