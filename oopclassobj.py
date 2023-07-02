class Employes:
    no_of_leaves=25 #class (variable) property //share variable  //rohan and amit are access
    pass

rohan=Employes()
amit=Employes()

rohan.salary=5000 #object property
rohan.role="teacher"
amit.salary=4000
amit.role="manager"

print(rohan.__dict__)
print(rohan.salary,rohan.no_of_leaves) #access data of object
rohan.no_of_leaves=35 #create new instance variable //no change class Employes value change //rohan no_of_leave is 35
print(rohan.__dict__) #print dict class old value 
print(Employes.no_of_leaves) #access data of class
print(Employes.__dict__) #print dict class old value //no_of_leave=25
Employes.no_of_leaves=30 # we change data for class //no change data object because it is class property for ex
                         # we change no_of_leaves value 25 to 30 for class// we not change no_of_leaves value for
                         #rohan and amit object
print(Employes.__dict__) #print dict class new value //no_of_leave=30
print(Employes.no_of_leaves)
