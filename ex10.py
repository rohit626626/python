#iris data
import requests
import pickle

data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris/data").text
l2=[item.split(",") for item in data.split("\n") if len(item)==0]
print(l2)

with open("myiris.pkl","wb") as f:
    pickle.dump(l2,f)


#to read
import pickle
with open ("myiris.pkl","rb") as f:
    print(pickle.load(f))