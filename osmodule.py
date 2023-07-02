import os
print(dir(os)) #print all os module 
print(os.getcwd()) #print current working dir
print(os.listdir()) #print all file in current working dir
print(os.listdir("F://")) #print all file in given path (F drive) working dir
#os.mkdir("myfol") #create new folder
#os.makedirs("fol1/fol2") #create folder inside folder (fol1 inside fol2)
# os.rename("fileold.py","filenew.py") #rename file (fileold.py to fileold.py)
print(os.environ.get("Path")) #print (set invorment path)
print(os.path.join("C://","myfiles.txt")) #join path 
print(os.path.exists("C://Program Files")) #print True and False //path are exist print true otherwisw false
print(os.path.isfile("C://Program Files")) #print True and False //file are exist print true otherwisw false
print(os.path.isdir("C://Program Files")) #print True and False //directry are exist print true otherwisw false
