import json

json_file_path = "review_pano.json"  # 파일 이름을 실제 파일의 이름으로 변경
with open(json_file_path, 'r', encoding= 'utf-8') as f:
    json_data = f.read()
    
data = json.loads(json_data)
    
print(data)


# "result" 안에 있는 "data"의 각 요소에서 "id" 추출
ids = [item["id"] for item in data["result"]["data"]]

print()
print(ids)

# "id"의 개수 출력
id_count = len(ids)
print("ID 개수:", id_count)