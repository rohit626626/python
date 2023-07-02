class Employes:
    def __init__(self, fname,lname, email):
        self.fname=fname
        self.lname=lname
        # self.email=f"{fname}.{lname}@gmail.com"
    def explain(self):
        return f"This employe is {self.fname} {self.lname}"

    @property #propert decorator change value of item for ex- we change email value
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email not set"
        return f"{self.fname}.{self.lname}@gmail.com"

    @email.setter #we change value help of setter of item
    def email(self,string):
        names=string.split("@")[0]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
    @email.deleter #we delete value help of deleter
    def email(self):
        self.fname=None
        self.lname=None


emp1=Employes("Sumit","kumar","Instructor")
emp2=Employes("Anil","singh","Worker")

print(emp1.explain())

print(emp1.email)#before decorator
emp1.fname="Sonu"
print(emp1.email)#after decorator


print(emp1.fname)#before setter
emp1.email="this.that@gmail.com" 
print(emp1.fname)#after setter

print(emp1.email)#befor deleter
del emp1.email
print(emp1.email)#after deleter