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
    "X-Cupix-Auth" : "eyJhbGciOiJIUzI1NiJ9.eyJ0b2tlbiI6ImF0NDlnenpjemU0OSIsImlzcyI6Imh0dHBzOi8vbm9haHRlc3Quc3RhZ2UuY3VwaXgud29ya3MiLCJpYXQiOjE3MDQ3ODMyMDUsImV4cCI6MTcwNDc4NjgwNSwidG9rZW5fdHlwZSI6ImFjY2Vzc190b2tlbiIsInNjb3BlIjpudWxsfQ.GMTZUg4_mZjftXsqdqUAXxXEEfbFfa-CCMU7ghh2myI"
} ## 토큰 줄바꿈 (\) 안되는지? 현재는 안됨 400에러 발생함

capture_id = '76089'
fields = 'id'

get_clusters_api_url = api_url + "clusters" + "?capture_id=" + capture_id + "&fields=" + fields

print('request url:', get_clusters_api_url)

res = requests.get(get_clusters_api_url, headers=headers)
print()
print(res)
print()
print(res.json())

JSON_file = res.json()

dir_name_1 = capture_id
wp_dir_name = pathlib.Path(dir_name_1)
wp_dir_name.mkdir(parents=True, exist_ok=True)

destination_folder = wp_dir_name
print()
print('destingation_folder:', destination_folder)

