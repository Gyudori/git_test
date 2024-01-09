# r(read)
file = open('i love python.txt', 'r', encoding='utf-8')
data = file.read()
print(data)
# 파일을 읽어 들여서 data라는 변수에 저장후 data 변수를 출력하는 기본적인 구조
file.close()