# reverse list three method
print("Enter the number one by one")
size=int(input("Enter the size of list: "))
mylist=[]
for i in range(size):
    mylist.append(int(input("Enter the list element: ")))

print(f"Your list is {mylist}")

reverse1=mylist[:]
reverse1.reverse()

reverse2=mylist[::-1]
print(f"My first reversed list of {mylist} is {reverse1}")
print(f"My second reversed list of {mylist} is {reverse2}")

reverse3=mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) - i- 1]= reverse3[len(reverse3) - i- 1],reverse3[i]

print(f"My third reversed list of {mylist} is {reverse3}")