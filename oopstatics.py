class Employes:
    no_of_leaves=25
    def __init__(self, ename,esalary, erole):
        self.name=ename
        self.salary=esalary
        self.role=erole


    @staticmethod
    def detail(string): #static method
        print("This is " + string)
        return "hello world"


sumit=Employes("Sumit",8000,"Instructor")
nitin=Employes("Nitin",7000,"Manager")

print(sumit.role)

print(nitin.detail("good person"))