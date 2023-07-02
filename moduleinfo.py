import sys #sys given path list, moduel are search and access data of location 
            #//first search current file,no current file data access,search data other path 
print(sys.path)

# user define moduel first type
import file5 #It is access data for file5.py //a=10 in file5.py //It is print 10 from file5 
print(file5.a)

#secound type
from file5 import a # this method simply print value of a but this method not use because 
                    #we import two file and secopund file in a=5 then generate  problen //
print(a)

# import sklearn as sk
# print(sk.__version__)
