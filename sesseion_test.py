# -*- coding: utf-8 -*-
import requests

# ���� ����
session = requests.Session()

# ������ ����ؼ� ���� ������ ��û
response = session.get("https://www.naver.com/")

# ���� ������ �ؽ�Ʈ�� ����
response_text = response.text

# �ؽ�Ʈ�� ���Ϸ� ���� (��: result.txt)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

# ������ HTML �ڵ带 ���
print(response.text)

