import os
import glob

path = "image"

listdir_result = os.listdir(path)
print(listdir_result) # 해당 폴더 안의 데이터만 보여줌


glob_result = glob.glob(f"{path}/*")  #f"{변수}/* : 모든 파일을 가져오기
print(glob_result) #지정한 경로와 해당 폴더 안의 데이터를 포함, '.'으로 시작한 파일명을 가져오지 않음