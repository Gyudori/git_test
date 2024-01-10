# -*- coding: utf-8 -*-
import json

## JSON ���� �����ϱ� 
oecd_cnty = {
    "AUS" : "호주",
    "AUT" : "오스트리아",
    "BEL" : "벨기에"
    }


file_path = "oecd_cnty.json"


with open(file_path, "w", encoding="cp949") as f:
    json.dump(oecd_cnty, f)
    

with open(file_path, "r", encoding='cp949') as f:
    oecd_cnty=json.load(f)
    # oecd_cnty=json.load(f, encoding="cp949")
print(oecd_cnty)