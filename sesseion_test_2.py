# -*- coding: utf-8 -*-
import requests

# 세션을 생성
session = requests.Session()

# 요청 파라미터 지정
parameter = {
    "search_category" : "value1",
    "search_categofy" : "value2",
}

# 세션을 사용해서 GET 요청을 수행
#response = session.get("https://www.example.com/search")
response = session.get("https://www.example.com/search", params=parameter)

response_text_2 = response.text

with open("result_2.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

# 응답의 HTML 코드를 출력
print(response_text_2)

# 세션 종료
session.close()