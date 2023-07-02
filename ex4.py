num=int(input("Pattern printing, Enter number how many row you want:"))
bool_val=input("1 for assinding order and 0 for desending order: ")
if bool_val=="1":
    for i in range(0,num+1):
        print("*"*i)

if bool_val=="0":
    for i in range(num,0,-1):
        print("*"*i)


