import requests
r=requests.get("https://google.com")
print(r.text)
print(r.status_code)


url="www.gmail.com"
data={
    "p1":4,
    "p2":5
}
r2=requests.post(url=url,data=data)
