class Employes:
    pub="This is public" #public all class access
    _pro="This is protected" #protcted main class and sub class access //protected class start underscore (_)
    __pri="This is private" #private class only access main class //private class start double underscore (__)


    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves


sumit=Employes("Sumit",8000,"Instructor")
anil=Employes("Anil",3000,"Worker")

print(sumit.pub) 
print(sumit._pro)
print(sumit._Employes__pri) # private class acess add _class name extra (_Employes) 