import time
tm1=time.time()
i=0
while(i<45):
    print("This is while loop",time.time()-tm1)
    i+=1
tm2=time.time()
for i in range(45):
    print("This is for loop",time.time()-tm2)

#local time 
loc=time.asctime(time.localtime(time.time())) #print curent time
print(loc)

#seek fun
for i in range(10):
    print("data 2 secound break then print")
    time.sleep(2)