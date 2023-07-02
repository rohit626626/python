#pickle module 
#insert data help of pickle module //data save in file binary mode
import pickle
cars=["audi","bmw","tata"]
file="mycar.pkl"
fileobj=open(file,"wb")
pickle.dump(cars,fileobj)
fileobj.close()

#access data help of pickle module
file="mycar.pkl"
fileobj=open(file,"rb")
mycar=pickle.load(fileobj)
print(mycar)