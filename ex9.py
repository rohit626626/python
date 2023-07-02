#News speaking
import requests
api_key="Your api key"
url=(f"news url={api_key}")
response=response.get(url)
data=response.json()

def speak(text):
    from win32.com.client import Dispatch
    speak=Dispatch("SAPI.Spvoicde")
    print(text)
    speak.speak(text)

for articles in data["articles"]:
    speak(articles['title'])
