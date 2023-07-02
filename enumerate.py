#enumerate fun 
l=["apple","banana","mengo","pineapple","date"]
for index,item in enumerate(l): #enumerate fun provide index and value for item, we simply use and perfome operation
                                #print 0,2,4 index value item
    if index%2==0:
        print(f"buy fruits {item}")
