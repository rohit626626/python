#list comp
l=[i for i in range(50) if i%3==0]
print(l)

#dic comp
dic={i:f"item {i}" for i in range(20) if i%3==0}
print(dic)

#reverse dic comp
dic={value:key for key,value in dic.items()}
print(dic)

#set comp
course={cor for cor in ["mba","mca","mba","mca","bca"]}
print(course)

#gen com
evens=(i for i in range(20) if i%2==0)
for item in evens:
    print(item,end=",")