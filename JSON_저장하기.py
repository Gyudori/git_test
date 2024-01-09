# -*- coding: utf-8 -*-
import json

## JSON 파일 저장하기
oecd_enty = {
    'AUS' : 'Australia',
    'AUT' : 'Austria',
    'BEL' : 'Belgium'
    }

## 딕셔너리를 json 파일로 저장하기 위해 경로를 설정.
file_path = 'oecd_cnty.json'

# 딕셔너리를 file_path에 맞게 .json 파일로 저장하는 코드.
with open(file_path, 'w', encoding='cp949') as f:
    json.dump(oecd_enty, f)

## JSON 파일 불러오기
with open(file_path, 'r', encoding='cp949') as f:
    oecd_cnty=json.load(f)
    # oecd_cnty=json.load(f, encoding='cp949')
# 불러오기 어떻게 전개되는지?