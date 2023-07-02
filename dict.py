dic={"rohan":"mba","mohan":"mca","amit":"bca"}
print(dic) #print complete dict
print(dic["mohan"]) #print mohan key value

dic1={"rohan":"mba","mohan":"mca","amit":{"car":"alto","mobile":"nokia"}} #dict inside dict
print(dic1)
print(dic1["amit"]) #print amit key value in dict
print(dic1["amit"]["car"]) #print amit 

dic2={"rohan":"mba","mohan":"mca","amit":"bca"}
dic2["sumit"]="bba" #add item in dict
del dic2["sumit"] #delete item (sumit)
print(dic2)

dic3=dic2.copy() #copy dic2 item in dic3
print(dic3)

dic4={"rohan":"mba","mohan":"mca","amit":"bca"} #print rohan key value
print(dic4.get("rohan"))

dic4.update({"rohan":"phd"}) #update value (rohan key value update mba to phd) //we add value it method, add new key and value
print(dic4)

print(dic4.keys()) #print all key values
print(dic4.items()) #print all keys and items values (key pair value)