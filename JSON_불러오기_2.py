# -*- coding: utf-8 -*-
import json

## JSON ���� �����ϱ� 
oecd_cnty = {
    'AUS' : 'ȣ��',
    'AUT' : '����Ʈ����',
    'BEL' : '���⿡'
    } # ��� �����ڵ� ���� �߻� ��� �ذ��ؾ� �ϴ���?

## ��ųʸ��� json ���Ϸ� �����ϱ� ���� ��θ� ����.
#file_path = 'oecd_cnty.json'
#
## ��ųʸ��� file_path�� �°� .json ���Ϸ� �����ϴ� �ڵ�.
#with open(file_path, 'w', encoding='cp949') as f:
#    json.dump(oecd_cnty, f)
#    
### JSON ���� �ҷ�����
#with open(file_path, 'r') as f:
#    oecd_cnty=json.load(f, encoding='cp949')
#    # oecd_cnty=json.load(f, encoding='cp949')