#self 
class Employes:
    def details(self):
        return f"Name is {self.name}, Salery is {self.salary} and role is {self.role}"


rohan=Employes()
amit=Employes()

rohan.name="Rohan"
rohan.salary=5000 
rohan.role="teacher"
amit.name="Amit"
amit.salary=4000
amit.role="manager"

print(rohan.details())

#self and __init__
class Employes:
    def __init__(self, ename,esalary, erole): #constructor example //__init__ method are take variable // it condition 
                                              # take 3 var ename, esalary and erole //this method take one time argument
                                              # and access time to time 
        self.name=ename
        self.salary=esalary
        self.role=erole


sumit=Employes("Sumit",8000,"Instructor")
anil=Employes("Anil",3000,"Worker")

print(sumit.salary)
print(anil.role)