#w(wirte)

file = open('i love python.txt', 'w', encoding= 'utf-8')
file.write('Hello, world!\n')
file.write('Welcome to Python!!\n')
file.close() # file.close()를 안쓰면 프로그램이 종료될때까지 해당 파일에 수정 불가능

# r(read)
file = open('i love python.txt', 'r', encoding= 'utf-8')
data = file.read()
print(data)
# 파일을 읽어 들여서 data라는 변수에 저장후 data 변수를 출력하는 기본적인 구조
file.close()