#import os

#folder_path = r'C:\Users\user\OneDrive\바탕 화면\23.05\SG135_서버용\방화벽'  # 변환할 폴더 경로 월마다 변경필요
#for file_name in os.listdir(folder_path):
#    if file_name.endswith('.log'):
#        file_path = os.path.join(folder_path, file_name)
#        with open(file_path, 'r', encoding='utf-8') as f:
#            text = f.read()
#        new_file_path = os.path.join(folder_path, file_name[:-4] + '.txt')
#        with open(new_file_path, 'w', encoding='ansi') as f:
#            f.write(text)
#        os.remove(file_path)  # 원본 .log 파일 삭제

##업그레이드 버전

import os

folder_paths = [
    r'C:\Users\next_\Desktop\24.05\SG105_본사\방화벽',
    r'C:\Users\next_\Desktop\24.05\SG135_서버용\WAF',
    r'C:\Users\next_\Desktop\24.05\SG135_서버용\방화벽',
    # 추가적인 폴더 경로들...
]

for folder_path in folder_paths:
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.log'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
            new_file_path = os.path.join(folder_path, file_name[:-4] + '.txt')
            with open(new_file_path, 'w', encoding='ansi') as f:
                f.write(text)
            os.remove(file_path)  # 원본 .log 파일 삭제