class Student:
    pass

rohan=Student() #object
amit=Student() #object

rohan.course="bba" #instance var
rohan.section="b" #instance var
amit.course="bca" #instance var
amit.section="a" #instance var
amit.sub=["c","c++","jave","php"] #instance var

print(rohan.course, amit.course,amit.sub)
