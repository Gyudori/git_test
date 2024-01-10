#-*- coding: utf-8 -*-
import requests
import glob
import pathlib
import os
import shutil
import json

path = 'request_test'

api_url= 'https://noahtest.stage.cupix.works/api/v1/'

headers = {
    "X-Cupix-Auth" : "eyJraWQiOiJieDJJNzFWVFAxZkI1elk1eUVyZFFVMkRpSUJ0V3RoUG81WllhQnE0QkpZPSIsImFsZyI6IlJTMjU2In0.eyJvcmlnaW5fanRpIjoiYzZmN2Q5YjgtNGY3MC00NDA0LTgxNWUtYTg3NGU4MzU1OWZiIiwic3ViIjoiZjU4OTVkNTUtMjBiNi00MDQ2LTlmN2ItMDI4YmZlNDllNGRmIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTcwNDg1MDM2NSwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfa3BQS1lzejhRIiwiZXhwIjoxNzA0ODU5NTI2LCJpYXQiOjE3MDQ4NTU5MjYsImp0aSI6ImUyYWFkOGJlLWY5MWItNDBhMy1iODc0LTI4ZWQxMjdjMWMyZCIsImNsaWVudF9pZCI6IjdiZ3ZmbW43bjU4bWdoOTh0aTZ2ODQ2ZmU0IiwidXNlcm5hbWUiOiJmNTg5NWQ1NS0yMGI2LTQwNDYtOWY3Yi0wMjhiZmU0OWU0ZGYifQ.dlF4SNIUXDONXTd2xDo3RGZruQVG2fRvNe4CZJIvu0AA8nU3AxCbgI9baYKU0hKpHjuwBpx7LPb0Fh83DDd-HIWO4jQsdB06s3Xe3kbPBDbpqnG0krMM7r7FGvVXjMaSKek_7rlDtUKX-s1paQJTaNw1EJqOjw6NWT9cXmtHbbuUy_0xoe9KylEyq_GaiDfFTZ2EBOnjxwSB95DTl8npHrNWZAzLJIHYzjKVREgY2FiONz1iusNqK8uXFdU9hhWUgyllflgveuzQVJeykwAO-2SUZBGBljLL4wqyV0FbKsKCtdj2d8hnPJe4N2iH9VjXQU8OkWFDxzntj9IyLgDOdA"
} ## 토큰 줄바꿈 (\) 안되는지? 현재는 안됨 400에러 발생함

capture_id = input("capture id:")
#capture_id = int(capture_id) # str > int 처리
fields = 'id'

get_clusters_api_url = api_url + "clusters" + "?capture_id=" + capture_id + "&fields=" + fields

print('request url:', get_clusters_api_url)

#res = requests.get(get_clusters_api_url) # response 401에러 발생 토큰을 못 받음
res = requests.get(get_clusters_api_url, headers=headers)
print()
print(res)
print()
print(res.json())

JSON_file = res.json()
file_path = 'JSON_file.json'

# 폴더 생성
dir_name_1 = capture_id
wp_dir_name = pathlib.Path(dir_name_1)
wp_dir_name.mkdir(parents=True, exist_ok=True)

destination_folder = wp_dir_name
print(destination_folder)
#JSON 파일 저장
with open(file_path,'w', encoding= 'cp949') as f: # encoding 유니코드, as f가 뭔지? 
    json.dump(JSON_file, f)
    
#JSON 파일 다른 폴더로 이동
shutil.move(file_path, destination_folder)