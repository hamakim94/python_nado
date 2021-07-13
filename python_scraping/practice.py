import requests
from requests import status_codes
res = requests.get("http://google.com")
res.raise_for_status()
print(len(res.text))
print(res.text)

with open("mygoogle.txt", "w", encoding= "utf-8") as f:
    f.write(res.text)