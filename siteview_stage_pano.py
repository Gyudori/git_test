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
    "X-Cupix-Auth" : "eyJraWQiOiJieDJJNzFWVFAxZkI1elk1eUVyZFFVMkRpSUJ0V3RoUG81WllhQnE0QkpZPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJmNTg5NWQ1NS0yMGI2LTQwNDYtOWY3Yi0wMjhiZmU0OWU0ZGYiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9rcFBLWXN6OFEiLCJjbGllbnRfaWQiOiI3Ymd2Zm1uN241OG1naDk4dGk2djg0NmZlNCIsIm9yaWdpbl9qdGkiOiJmYjA4YmMwMy1jYzJiLTQxODYtODk4OS1mZDEzN2VlMDA2ZTUiLCJldmVudF9pZCI6IjE5MWEzMTJlLTI3N2EtNDY4Yy05ZmUwLTg0MzVjMjI1NDYyMyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3MDUyMzg4MzcsImV4cCI6MTcwNTMyMTU5NiwiaWF0IjoxNzA1MzE3OTk2LCJqdGkiOiI3MGFkMDliZS1jYzI3LTRiZDUtODQ5Ny0wMjc1OWU3ZGE0MWUiLCJ1c2VybmFtZSI6ImY1ODk1ZDU1LTIwYjYtNDA0Ni05ZjdiLTAyOGJmZTQ5ZTRkZiJ9.t8rnzepFLqsIjhq7tkuXTxQJK3WHgihXe3lamVrL2LwSbwMsNe3FLGoxeT8IA2TEp_U_nysQieWC-vfEpZXgnki0vvT3Oek9e87lM0H9-QV8a69FKwqwU1P0Zcb5H5kVXs9srOBZYhaAg3McRaiDwRDH62KE6aiYBJ6u5BrppHZUmGL4p3Zg7R__-kv67kWVOXLlS8xC0nRtqLYTPUMS6nWUYeHysCNXg0I25Y2FfU2pch8gbtEehuzfo40YpzCBYGmy25WZDdapyU6RHzUqFMH6V9T1jSKJ8bnzlwLsLKoHujNJZASFKybStAa4wjsU5UDbDLM2Jf6pa1_z--8Ylw"
}

review_key = input("review key:")
# fields 값 1개 이상 좋게 하는 방법 없나??
fields = input('fileds: ') # , 필수

get_pano_api_url = api_url + review_key + "/panos?fields=" + fields

print(get_pano_api_url)
res = requests.get(get_pano_api_url, headers=our_header) # 응답 콜

#def get_api_data(page=1, per_page=30):
#    
#    params = {'page': page, 'per_page': per_page}
#
#    response = res
#
#    if response.status_code == 200:
#        return response.json()
#    else:
#        print(f"Error: {response.status_code}")
#        return None
#
#def extract_data():
#    total_items = 0
#    page = 1
#
#    while True:
#        data = get_api_data(page)
#        
#        if not data:
#            break
#
#        # 여기에서 데이터 추출 또는 처리 작업 수행
#        for item in data:
#            # 예: 원하는 작업 수행
#            print(item)
#
#        total_items += len(data)
#        page += 1
#
#    print(f"Total items extracted: {total_items}")
#
## 실행
#extract_data()
#
#print(extract_data()) # 루프 묶임


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