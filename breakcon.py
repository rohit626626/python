#break and continue
i=0
while(True): #while(True) and while(1) are  done same work 
    if i<5:
        i=i+1 
        continue #continue statement (skep it item and looping again)
    print(i, end=" ")
    if i==45:
        break #break statement (statement true loop break)
    i=i+1

#quiz
while(True):

    num=int(input("Enter a number: "))
    if num>100:
        print("congrlaute, You number greater 100")
        break
    else:
        print("Try again")
        continue
