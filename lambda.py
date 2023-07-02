# add two number without lambda function
# def add(a,b):
#     return(a+b)
# print(add(2,4))

#lambda function or anonymous function
#lambda function  small method of add(other operation) two number //we not create function //lambda function no name
add=lambda a,b:a+b #code small for lambda function
print(add(2,4))

#secound example lambda function
l=[[9,8],[7,6],[5,4],[3,2]] 
l.sort(key=lambda x:x[1]) # lambda return list in assinding order
print(l)