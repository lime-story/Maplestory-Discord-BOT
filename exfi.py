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


#캐릭터 스펙정보 출력
charinformation = ("https://open.api.nexon.com/maplestory/v1/character/basic?ocid="+response.json()["ocid"])
char_response = requests.get(charinformation, headers=headers)
char_response.json

#디버깅 "캐릭터 정보 출력"
print(char_response.json())

#정보 출력 정리
charin = char_response.json()

#캐릭정보 함수
character_name = charin.get("character_name")
world_name = charin.get("world_name")
character_class = charin.get("character_class")
character_level = charin.get("character_level")
character_exp = charin.get("character_exp")
character_exp_rate = charin.get("character_exp_rate")
character_guild_name = charin.get("character_guild_name")
character_image = charin.get("character_image")


print(f"닉네임 : {character_name} \n서버 : {world_name}\n직업 : {character_class}\n레벨 : {character_level}\n경험치 : {character_exp_rate}%\n길드 : {character_guild_name}\n캐릭터 사진 : {character_image}")
