#health management system
client_list={1:"Harry",2:"Rohan",3:"Hammad"}
log_list={1:"Exercise",2:"Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()



try:
    print("Select client name: ")
    for key, value in client_list.items():
        print("Press",key, "for",value, "\n", end="")
    client_name=int(input())

    print("Selected client: ",client_list[client_name],end="")

    print("Press 1 for log")
    print("Press 2 for retrieve")
    op=int(input())

    if op is 1:
        for key, value in log_list.items():
            print("Press",key, "to lock",value, "\n", end="")
        log_name=int(input())
        print("Selected job: ",log_list[log_name])
        f=open(client_list[client_name] +"_", log_list[log_name]+ ".txt", "a")
        k="y"
        while(k is not "n"):
            print("Enter" ,log_list[log_name], "\n", end="")
            mytext=input()
            f.write("[" + str(getdate())+ "]:" + mytext + "\n")
            k=input("Add more ? y/n: ")
            continue
        f.close()


    elif op is 2:
        for key, value in log_list.items():
            print("Press",key, "to retrieve",value, "\n", end="")
        log_name=int(input())
        print(client_list[client_name],"_", log_list[log_name],"Report: ","\n", end="")
        f=open(client_list[client_name]+"_"+ log_list[log_name] + ".txt", "rt")
        contents=f.readlines()
        for line in contents:
            print(line, end="")
        f.close()
    else:
        print("invalid input")
except Exception as e:
    print("Wrong input")



