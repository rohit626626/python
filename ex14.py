#apple devided
apples=int(input("Enter the number apple of: "))
mn=int(input("Enter the minium number of apple: "))
mx=int(input("Enter the maxium number of apple: "))

for i in range(mn, mx+1):
    if apples%i==0:
        print(f"{i} is a divider of {apples}")
    else:
        print(f"{i} is not a divider of {apples}")