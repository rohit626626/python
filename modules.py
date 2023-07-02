import random
num1=random.randint(1,100) #print value 1 to 100
print(num1)

num2=random.random() #print float value lessthen 1
print(num2)

num3=random.random()*100 #print float value lessthen 100 because we multiply 100
print(num3)

l=["Aaj tak","Star gold","Sony mix","DD sport"]
ch=random.choice(l) #choice function print one chanel in list (randomely)
print(ch)