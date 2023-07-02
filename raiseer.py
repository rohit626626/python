# inp=input("Enter your name: ")
# if inp.isnumeric():
#     raise Exception("Number not allow") # if user given wrong input number in string input
#                                     #raise function handel it error print exception message and program break
# print(f"hello {inp}")

# #zero devision error
# inp1=int(input("Enter first number: "))
# inp2=int(input("Enter secound number: "))
# if inp2==0:
#     raise ZeroDivisionError("inp2 is 0")
# ot=inp1/inp2
# print(ot)

#try except
inp3=input("Enter your name: ")
try:
    print(a)
except Exception as e:
    if inp3=="sonu":
        raise ValueError("sonu is block")
    print(f"exception handel, your input is {inp3}")
