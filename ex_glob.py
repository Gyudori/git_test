import glob
import os

path = "image"

#result = glob.glob(f"{path}/*") #해당 폴더에 모든 파일들을 가져오기
#result_text = glob.glob(f"{path}/*.txt") #txt 파일만 가져오기
#result_py = glob.glob(f"{path}/s*.py") # py파일 중 's'로 시작한 파일 가져오기
#
#print(result)
#print()
#print(result_text)
#print()
#print(result_py)

result = []
#for i in glob.glob(f"{path}/*"):
#    if os.path.isdir(i):    #os.path.isdir() : 폴더인지 확인
#        result.append(i)
#print(result)

for i in glob.glob(f"{path}/*"):
    if os.path.isfile(i):    #os.path.isfile() : 파일인지 확인 (is~)
        result.append(i)
print(result)

# 위랑 같은 결과
result_1 = filter(os.path.isdir, glob.glob(f"{path}/*"))
print(list(result_1))