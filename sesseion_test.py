# -*- coding: utf-8 -*-
import requests

# 세션 생성
session = requests.Session()

# 세션을 사용해서 메인 페이지 요청
response = session.get("https://www.naver.com/")

# 응답 내용을 텍스트로 저장
response_text = response.text

# 텍스트를 파일로 저장 (예: result.txt)

with open("result.txt", "w", encoding="utf-8") as file:
    file.write(response.text)

# 응답의 HTML 코드를 출력
print(response.text)

