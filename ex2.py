#faulty calculator
inp1=input("Operator: ")
inp2=input("Enter first number: ")
inp3=input("Enter secound number: ")

ans=inp2+inp1+inp3

if ans=="45*3":
    print(555)
elif ans=="56+9":
    print(77)
elif ans=="56/4":
    print(4)
elif inp1=="*":
    print(int(inp2) * int(inp3))
elif inp1=="-":
    print(int(inp2) - int(inp3))
elif inp1=="+":
    print(int(inp2) + int(inp3))
elif inp1=="/":
    print(int(inp2) / int(inp3))