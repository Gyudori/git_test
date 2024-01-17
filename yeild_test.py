def return_abc():
    return list("ABC")

def yield_abc():
    yield "A"
    yield "B"
    yield "C"
    
for ch in return_abc():
    print(ch)
print()    
for ch_2 in yield_abc():
    print(ch_2) 
    
print()
print(return_abc()) # 리스트 반환
print()
print(yield_abc()) # 제너레이터 반환

