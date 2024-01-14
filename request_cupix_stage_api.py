#-*- coding: utf-8 -*-
import requests
import glob
import pathlib
import os
import shutil
import json

path = 'request_test'


#api_url= f'https://{region}.{domain}.stage.cupix.works/api/v1/'

api_url= 'https://noahtest.stage.cupix.works/api/v1/'

# region 설정
if 'eu' in api_url:
    region = 'eu'
elif 'au' in api_url:
    region = 'au'
else:
    region = 'us'

# https:// 제거
domain = api_url.replace('https://','')
# '.'기준으로 나누기
domain = domain.split('.')
# domain 설정
domain = domain[0]

our_header = {
    "X-Cupix-Auth" : "eyJraWQiOiJieDJJNzFWVFAxZkI1elk1eUVyZFFVMkRpSUJ0V3RoUG81WllhQnE0QkpZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJmNTg5NWQ1NS0yMGI2LTQwNDYtOWY3Yi0wMjhiZmU0OWU0ZGYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9rcFBLWXN6OFEiLCJjbGllbnRfaWQiOiI3Ymd2Zm1uN241OG1naDk4dGk2djg0NmZlNCIsIm9yaWdpbl9qdGkiOiJmYjA4YmMwMy1jYzJiLTQxODYtODk4OS1mZDEzN2VlMDA2ZTUiLCJldmVudF9pZCI6IjE5MWEzMTJlLTI3N2EtNDY4Yy05ZmUwLTg0MzVjMjI1NDYyMyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3MDUyMzg4MzcsImV4cCI6MTcwNTI0MjQzNiwiaWF0IjoxNzA1MjM4ODM3LCJqdGkiOiJmZWEzY2FjNi1kNDE0LTQ1MmQtYTg4My1kYmRkZmM5MTc0NzciLCJ1c2VybmFtZSI6ImY1ODk1ZDU1LTIwYjYtNDA0Ni05ZjdiLTAyOGJmZTQ5ZTRkZiJ9.HMV2B8079ycEzZAUPoQI80B66_KoAF8bn77-uO8WxjcIlZrOsG3xcUsPhb5FbflZ-tEw-Nz2M4bgBh589o7dsGk1pj7qK5sbdQ1gV-wBN-l5rlcSyiASHSCu8zA5ZVBcvYXl5KjQAdNxo6uJpyeCNrb7SU8OiuU9yzyIb3Y8DOviWlhjic5XwrAdLyV1rJ5P_SweT7uoTUJ6K6WfhOtTxTy8BhWYJ7OR_W130Tb5fSf5jM0kuyZbLy12gZIeYKM7BWUCjviZJ0gSLkMgBadLCOTfInSkJF6KZilJzdXfeqjyb2v19px4nbBBd6L6nZCewDhGAtKPlW2h0stgiZ2Atg"
} ## 줄바꿈 적용 안되는지? > '\' 하면 400에러 발생

capture_id = input("capture id:")
# capture_id = '76089'

fields = 'id'

get_clusters_api_url = api_url + "clusters" + "?capture_id=" + capture_id + "&fields=" + fields

print('request url:', get_clusters_api_url)

#res = requests.get(get_clusters_api_url) # response 401 headers를 왜? 이렇게 표기하는지?
res = requests.get(get_clusters_api_url, headers=our_header)
print()
print(res)
print()
print(res.json())
print()

# 파일 이름 설정
dir_name_1 = region + '_' + domain + '_' + capture_id
wp_dir_name = pathlib.Path(dir_name_1)
wp_dir_name.mkdir(parents=True, exist_ok=True)

file_name = 'clusters.json'
json_filepath = wp_dir_name.joinpath(file_name)

print(json_filepath)
print()
clusters_json = res.json()

with open(json_filepath,'w', encoding= 'cp949') as f:  
    json.dump(clusters_json, f)



destination_folder = wp_dir_name
print(destination_folder)
#JSON 저장

    
##JSON 생성한 폴더로 이동
#shutil.move(file_path, destination_folder)