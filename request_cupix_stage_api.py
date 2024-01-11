#-*- coding: utf-8 -*-
import requests
import glob
import pathlib
import os
import shutil
import json

path = 'request_test'

domain = 'noahtest'

region = 'eu'

#api_url= f'https://{region}.{domain}.stage.cupix.works/api/v1/'

api_url= 'https://noahtest.stage.cupix.works/api/v1/'

our_header = {
    "X-Cupix-Auth" : "eyJraWQiOiJieDJJNzFWVFAxZkI1elk1eUVyZFFVMkRpSUJ0V3RoUG81WllhQnE0QkpZPSIsImFsZyI6IlJTMjU2In0.eyJvcmlnaW5fanRpIjoiZDY3ZmExNjAtODRmNS00N2RhLTlmYTgtYzMxM2U2NThkNjExIiwic3ViIjoiZjU4OTVkNTUtMjBiNi00MDQ2LTlmN2ItMDI4YmZlNDllNGRmIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTcwNDk0MjkyMSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfa3BQS1lzejhRIiwiZXhwIjoxNzA0OTQ2NTIxLCJpYXQiOjE3MDQ5NDI5MjEsImp0aSI6ImM5NTU5NmMwLWJlMWItNDg4Yi1hYmQwLTg0NzFjZGM3ZjM5ZiIsImNsaWVudF9pZCI6IjdiZ3ZmbW43bjU4bWdoOTh0aTZ2ODQ2ZmU0IiwidXNlcm5hbWUiOiJmNTg5NWQ1NS0yMGI2LTQwNDYtOWY3Yi0wMjhiZmU0OWU0ZGYifQ.PsX0uc-itB95KGdFER7dKd6tUnGftl6aFY8lZHZAhMCYrf_b6_QpFy7r9fO_XsD2BbFFYm7_99WMsQ9o-PNE58EUssDsl0qNeOmqeQZI8YPkULriwIZcc7M2DYQStvFkHVO2VyIexvityBVIBtUMRJgsazpeskWDdUwHi3tDW3MumEjy8BHnF1mrX4wpjlMLaAmiGB_PqDZJGqRvmNxXvM6wykrzSQHDiLN8jou4VU_mAVmxB5XXjBkII78sWQYELwGtLUlKuD6_wY1k-gZLglmdCwi_mn5l44p8jrCzrzvMiIAjas97mWlrheQwm9Fn0kSR6FFs0V8tOjrIM8LGBA"
} ## 줄바꿈 적용 안되는지? > '\' 하면 400에러 발생

# capture_id = input("capture id:")
capture_id = '76089'

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