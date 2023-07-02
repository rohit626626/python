# "r" for reading //default
f=open("file1.py")

# f=open("file1.py","r") #read mode
# f=open("file1.py","rt") #text mode
# f=open("file1.py","rb") #binary mode

# content=f.read(12) # print 12 char
# print(content)

#with open fun
with open("file1.py") as f: #with open function open file and automatic close file// we not close file 
    a=f.read(5)
    print(a)

# print(f.readline()) #print first line
# print(f.tell()) #print curront cursor position
# print(f.readline()) #print next(secound line)
# print(f.seek(0)) #change cursor position (0) //data read 0 position
# print(f.readline()) #print next(secound line)
# print(f.seek(10)) #change cursor position (10) // data read 11 char position
# print(f.readline()) #print next(secound line)


# print(f.readlines()) #print data in dict

#for loop
# for line in content: # print char by char
#     print(line)

# for line in f: # print word by word
#     print(line)


#write file
# f=open("file2.txt","w") 
# a=f.write("php is a scripting language")# w mode add data in file //data override //file not esist file create
# print(a) #print char length


# f=open("file4.txt","a") #append data in end, not override //file not esist file create
# f.write("It is popular language")

#read and write mode
# f=open("file2.txt","r+") #r+ mode read and write data // r+ mode write data in bigning and  override data in begining 
#                          #// r+ mode not create file //file not esist given error
# f.write("Thank you")
# print(f.read())



# "w" for writing
# "x" create file not esist
# "a" append end 
# "t" text mode
# "b" binary mode
# "+" read and write mode



f.close()