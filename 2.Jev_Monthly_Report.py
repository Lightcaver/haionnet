import os
import pandas as pd

# 여러 개의 폴더 경로 정의
directories = [
    #'C:/Users/next_/Desktop/24.05/SG105_본사/방화벽'
    #'C:/Users/next_/Desktop/24.05/SG135_서버용/방화벽'
    'C:/Users/next_/Desktop/24.05/SG135_서버용/WAF',
    # 추가적인 폴더 경로들...
]

for directory in directories:
    # 폴더 내 TXT 파일 불러오기
    txt_files = [f for f in os.listdir(directory) if f.endswith('.txt')]

    for file in txt_files:
        file_path = os.path.join(directory, file)
        print(f"Processing file: {file_path}")

        # TXT 파일 읽어들이기
        with open(file_path, 'r') as f:
            data = [line.split() for line in f]

        # 데이터를 DataFrame으로 변환
        df = pd.DataFrame(data)

        # 엑셀 파일 저장
        excel_file = os.path.join(directory, file.replace('.txt', '.xlsx'))
        df.to_excel(excel_file, index=False, header=False)
        print(f"{excel_file} saved.")

        # 필터링 적용 (예시: 첫 번째 열의 값이 '='인 행만 선택)
        filtered_df = df[df.iloc[:, 0] == '=']

        # 필터링된 데이터 엑셀 파일로 저장
        filtered_excel_file = os.path.join(directory, file.replace('.txt', '_filtered.xlsx'))
        filtered_df.to_excel(filtered_excel_file, index=False, header=False)
        print(f"{filtered_excel_file} saved.")

print("Processing complete.")