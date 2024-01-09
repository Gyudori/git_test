import requests
import glob
import pathlib
import os
import shutil

path = 'request_test'

api_url= 'https://cupix.cupix.works/api/v1/'

headers = {
    "X-Cupix-Auth" : "eyJraWQiOiJieDJJNzFWVFAxZkI1elk1eUVyZFFVMkRpSUJ0V3RoUG81WllhQnE0QkpZPSIsImFsZyI6IlJTMjU2In0.eyJvcmlnaW5fanRpIjoiZmViNzc5YWQtZmM2YS00YzVjLWE3OTgtZDdkNjcwYzRlNTgyIiwic3ViIjoiZjU4OTVkNTUtMjBiNi00MDQ2LTlmN2ItMDI4YmZlNDllNGRmIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJhd3MuY29nbml0by5zaWduaW4udXNlci5hZG1pbiIsImF1dGhfdGltZSI6MTcwNDc3MDAyMiwiaXNzIjoiaHR0cHM6XC9cL2NvZ25pdG8taWRwLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tXC91cy13ZXN0LTJfa3BQS1lzejhRIiwiZXhwIjoxNzA0NzczNjIyLCJpYXQiOjE3MDQ3NzAwMjIsImp0aSI6ImFhNTFiYThmLWJiNTgtNGMzYy04OTQ3LTU2NDdlZDA5OGViNCIsImNsaWVudF9pZCI6IjdkZDdoMTVhcGk1aXIxbHZxdGk1azluZnJvIiwidXNlcm5hbWUiOiJmNTg5NWQ1NS0yMGI2LTQwNDYtOWY3Yi0wMjhiZmU0OWU0ZGYifQ.rB6NP7EeNA25rzHhj0nEuXlZ7AK7TTtOI_TcwxwExBYtkGDXPgFxijnGJgVqNntJIt4tkApYAu3mvhJzdiLoTI95d2LPqr6vCfjay_vjt5V2VM3fmVuGAsI6Mzm6N7pgDKssGtTkra3B0EOOAIW9CYSuKGPSFbEVxGiDVKz4HLwni_Ek_lRHKH8Q5txJac4XtMvjDMFhSopIL54e9WUfKL2nn8xWgT8_moTR53YNDbhAmK3BTKG6_qdRJgUPN00UjhTXdhD8hTVCka08HdTfZ-IkmyeUzz2PN-GPMNBAWHsBQjerzGkvfcTTUKVN58Qav66tS0lQuSpy-TMTmcE0ig"
}

capture_id = '283844'
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

# JSON ?åå?ùº ?ù¥?èô ?ï®?àò ?ò∏Ï∂?
shutil.move(destination_folder)