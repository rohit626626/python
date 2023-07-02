class Employes:
    def __init__(self, fname,lname, email):
        self.fname=fname
        self.lname=lname

    def explain(self):
        return f"This employe is {self.fname} {self.lname}"



emp1=Employes("Sumit","kumar","Instructor")
emp2=Employes("Anil","singh","Worker")

print(type(emp1)) #print object type
print(id(emp1)) #print object id
print(dir(emp1)) #print complete list of item, we perfome action
