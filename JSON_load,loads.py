import json
#주의 변수 data는 dict가 아닌 ' 문자열 ' 이다.
data = '{"id":"01", "language":"korean","edition":"third", "author":"wonwoo joo"}'

jdata = json.loads(data) # 문자열을 읽을 때
print(jdata)

# data를 json파일로 저장

data = {"id":"1000", 
		"language":{"first":"korean","seconds":"english"}, 
		"grade":"A", "name":"honaldo"}

with open ("jsondata.json", "w", encoding="utf-8-sig") as json_file:
    jdata = json.dump(data, json_file, indent=2)


# load 저장한 json 파일을 읽기 
with open ("jsondata.json", "r", encoding="utf-8-sig") as json_file:
    jdata = json.load(json_file)
    print(jdata)