# 현재 폴더(디렉토리) 확인 os: os.getcwd(), pathlib: pathlib.Path.cwd()
# 파일 또는 폴더 존재여부 os: os.path.exists(dir_name), pathlib: pathlib.Path(dir_name).exist()
# 폴더 만들기 os: os.makedirs(dir_name), pathlib: pthlib.Path(dir_name).mkdir()
# 파일 및 폴더 확인 os: os.listdir(dir_name), pathlib: pathlib.Path(dir_name).glob('*')
# 상위 폴더 확인 os: os.path.dimame(dir_name), pathlib: pathlib.Path(dir_name).parent
# 경로 연결 os: os.path.join(dir1,dir2), pathlib: pathlib.Path(dir1).joinpath(dir2)
# 파일명과 확장자 분리 os: os.path.splitext(file_name), pathlib: pathlib.Path(file_name).stem, pathlib.Path(file_name).suffix


import os
import pathlib
# 현재 폴더(디렉토리) 확인하기
print('os 모듈=', os.getcwd())
print('pathlib 모듈=', pathlib.Path.cwd())

# 파일 또는 폴더 존재 여부
dir_name = 'C:/Users/QA/Desktop/픽픽' # 역슬래시 아님
file_name = 'C:/Users/~/Desktop/image/_2.jpg'
print(os.path.exists(dir_name)) # 폴더가 존재하는지?
print(os.path.exists(file_name)) # _2 파일이 존재하는지?

path_1 = pathlib.Path(dir_name) # Path 객체로 변환
path_2 = pathlib.Path(file_name)

print("path_1.exists:", path_1.exists()) # 폴더가 존재하는지?
print(pathlib.Path.exists(path_2)) # 파일이 존재한는지?

# 폴더 만들기
dir_name_1 = './parent_folder/child_folder/child_folder_2'
os.makedirs(dir_name_1, exist_ok=True)

wp_dir_name = pathlib.Path(dir_name_1)
wp_dir_name.mkdir(parents=True, exist_ok=True) # parents를 True해야 폴더 생성할 수 있음

# 파일과 폴더 확인
print(os.listdir('./parent_folder'))
p = pathlib.Path('./parent_folder').glob('*')
list_p = list(p)
print(list(p)) # os.listdir과는 다르게 문자열이 아닌 Path 객체의 리스트가 반환

# 상위 폴더 확인
cur_dir = os.getcwd() # 현재 디렉토리
print(os.path.dirname(cur_dir))

wp_cur_dir = pathlib.Path(cur_dir)
print(wp_cur_dir.parent)

# 경로 연결 -> 디렉토리 + 디렉토리 또는 디렉토리 + 파일 연결
parent_dir_name = './parent_folder'
child_dir_name = 'child_folder'
print('os:' ,os.path.join(parent_dir_name,child_dir_name) )
print('pathlib:' , pathlib.Path(parent_dir_name).joinpath(child_dir_name) )

# 파일명과 확장자 분리
file_path = 'empty2.v.1.txt'
print(os.path.splitext(file_path))

path = pathlib.Path(file_path)
print(path.stem, path.suffix)

