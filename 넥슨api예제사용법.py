#넥슨 API 방법 파이썬


import requests
from bs4 import BeautifulSoup

headers = {"x-nxopen-api-key": "넥슨 API키"}
name = input()
usernames = "https://open.api.nexon.com/maplestory/v1/id?character_name=" + name 
response = requests.get(usernames, headers = headers)

#디버깅 라인
print(response.json())
print(response.json()["ocid"]) 
print("https://open.api.nexon.com/maplestory/v1/character/basic?ocid="+response.json()["ocid"])

#ocid (그 캐릭터의 고유의 코드) 