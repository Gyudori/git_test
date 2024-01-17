# -*- coding: utf-8 -*-
import requests

# ������ ����
session = requests.Session()

# ��û �Ķ���� ����
parameter = {
    "search_category" : "value1",
    "search_categofy" : "value2",
}

# ������ ����ؼ� GET ��û�� ����
#response = session.get("https://www.example.com/search")
response = session.get("https://www.example.com/search", params=parameter)

response_text_2 = response.text

with open("result_2.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

# ������ HTML �ڵ带 ���
print(response_text_2)

# ���� ����
session.close()