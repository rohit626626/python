num1=input("Enter first number: ")
num2=input("Enter secound number: ")
try:
    print(int(num1) + int(num2)) #supose, user given input string
except Exception as e:
    print(e)

print("imp msg")