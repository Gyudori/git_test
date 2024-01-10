import json

dictionary = {
    "id" : "04",
    "name" : "Jun",
    "department" : "HR"
}

# Python dict object를 JSON 문자열로 변환한다.
# 문법: json.dumps(dict, indent)
# 인자: dict - dictionary의 이름, indent - 들여쓰기 숫자
json_obect = json.dumps(dictionary, indent= 3)

print(json_obect)
print()

# json.dump() 메서드는 JSON 파일에 write 하는데 사용
# 문법: josn.dump(dict, file_pointer)
# 인자: ict - dictionary의 이름, file pointer - 저장하고자 하는 파일 object

with open("test.json", "w") as f:
    json.dump(dictionary, f)
    
