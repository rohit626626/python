# age program
yearAge=int(input("Enter your Age/Year of Birth: "))
isAge=False
isYear=False

if len(str(yearAge))==4:
    isYear=True

else:
    isAge=True

if(yearAge<1900 and isYear):
    print("You seem to oldest person alive")
    exit()

if(yearAge>2019):
    print("you are not yet born")
    exit() 

if isAge:
    yearAge=2019 - yearAge
    print(f"you will be 100 years old in {yearAge+100}")

interesdYear=int(input("Enter the year you want to know your age in: "))
print(f"you will be {interesdYear - yearAge} years old in {interesdYear}")
