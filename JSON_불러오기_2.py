# -*- coding: utf-8 -*-
import json

## JSON 파일 저장하기 
oecd_cnty = {
    'AUS' : '호주',
    'AUT' : '오스트리아',
    'BEL' : '벨기에'
    } # 계속 유니코드 에러 발생 어떻게 해결해야 하는지?

## 딕셔너리를 json 파일로 저장하기 위해 경로를 설정.
#file_path = 'oecd_cnty.json'
#
## 딕셔너리를 file_path에 맞게 .json 파일로 저장하는 코드.
#with open(file_path, 'w', encoding='cp949') as f:
#    json.dump(oecd_cnty, f)
#    
### JSON 파일 불러오기
#with open(file_path, 'r') as f:
#    oecd_cnty=json.load(f, encoding='cp949')
#    # oecd_cnty=json.load(f, encoding='cp949')