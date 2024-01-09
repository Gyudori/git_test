# -*- coding: utf-8 -*-
import json

## JSON ���� �����ϱ�
oecd_enty = {
    'AUS' : 'Australia',
    'AUT' : 'Austria',
    'BEL' : 'Belgium'
    }

## ��ųʸ��� json ���Ϸ� �����ϱ� ���� ��θ� ����.
file_path = 'oecd_cnty.json'

# ��ųʸ��� file_path�� �°� .json ���Ϸ� �����ϴ� �ڵ�.
with open(file_path, 'w', encoding='cp949') as f:
    json.dump(oecd_enty, f)

## JSON ���� �ҷ�����
with open(file_path, 'r', encoding='cp949') as f:
    oecd_cnty=json.load(f)
    # oecd_cnty=json.load(f, encoding='cp949')
# �ҷ����� ��� �����Ǵ���?