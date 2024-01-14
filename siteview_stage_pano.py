import requests
import json
import os
import glob
import pathlib

path = 'pano_id'

api_url = 'https://noahtest.stage.cupix.works/api/v1/reviews/' #m967vu/panos?fields=id

# region 설정
if 'eu' in api_url:
    region = 'eu'
elif 'au' in api_url:
    region = 'au'
else:
    region = 'us'
    
# domain 설정
domain = api_url.replace('https://','')
domain = domain.split('.')
domain = domain [0]

#토큰 dictionary
our_header = {
    "X-Cupix-Auth" : "eyJraWQiOiJieDJJNzFWVFAxZkI1elk1eUVyZFFVMkRpSUJ0V3RoUG81WllhQnE0QkpZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJmNTg5NWQ1NS0yMGI2LTQwNDYtOWY3Yi0wMjhiZmU0OWU0ZGYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9rcFBLWXN6OFEiLCJjbGllbnRfaWQiOiI3Ymd2Zm1uN241OG1naDk4dGk2djg0NmZlNCIsIm9yaWdpbl9qdGkiOiJmYjA4YmMwMy1jYzJiLTQxODYtODk4OS1mZDEzN2VlMDA2ZTUiLCJldmVudF9pZCI6IjE5MWEzMTJlLTI3N2EtNDY4Yy05ZmUwLTg0MzVjMjI1NDYyMyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3MDUyMzg4MzcsImV4cCI6MTcwNTI0NjEyNCwiaWF0IjoxNzA1MjQyNTI0LCJqdGkiOiI5NDBjNDE5Zi02NmM1LTQyNzEtODU2Mi1jMWYzNDlmZDc0OTQiLCJ1c2VybmFtZSI6ImY1ODk1ZDU1LTIwYjYtNDA0Ni05ZjdiLTAyOGJmZTQ5ZTRkZiJ9.IFh1oxxZ8-JjOy0KVyeZm-R7dJ7gTH5UpGP4mimU07V8_3OGr8BqRpXpFAIA5jVshG5mJc6AgcbRWD-UmagTZ_xO88vgwPz9n9piyoP4h-LbX6m_2R6SDFO2OotsY4jI_6BtFHAgS37pBc4F9GExugMksNhD0YQbIJm_xLV9YzsTszrKFQHSJ0OlolyIIoG8KtB4NkDKPknj2rC_XWSO-42-FGrAT062n0RyeCCVvitGvKw6q-iFNV3L8LrQwjDohdcIbx6dywvcAkdchKmFf2el6e_EoYGyRkGs_Vk_M7lgdja6NsWqdYr8z0mhaBqOkOeSFCuQhpMIg8Y1daNPew"
}

review_key = input("review key:")
# fields 값 1개 이상 좋게 하는 방법 없나??
fields = 'id,name' 

get_pano_api_url = api_url + review_key + "/panos?fields=" + fields

print(get_pano_api_url)
res = requests.get(get_pano_api_url, headers=our_header)

# 파일 이름 설정
folder_name = region + '_' + domain + '_' + review_key
# 파일 생성
wp_dir_name = pathlib.Path(folder_name)
wp_dir_name.mkdir(parents=True, exist_ok= True)

# JSON 파일 생성
file_name = 'review_pano.json'
json_filepath = wp_dir_name.joinpath(file_name)
review_pano_json = res.json() # total page를 어떻게 불러오는지?? > 현재는 jSON 1페이지만 불러옴

# JSON 파일 폴더에 저장
with open(json_filepath, 'w', encoding= 'cp949') as f:
    json.dump(review_pano_json, f, indent= 4)
    
destination_folder = wp_dir_name
print(destination_folder)