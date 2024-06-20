import os
import pandas as pd

# 디렉토리 경로 설정
directory_paths = [
    r'C:/Users/next_/Desktop/24.05/SG105_본사/방화벽'
    #r'C:/Users/next_/Desktop/24.05/SG135_서버용/방화벽'
]

# 모든 디렉토리에서 파일 목록 가져오기
file_list = []
for directory_path in directory_paths:
    file_list.extend([file for file in os.listdir(directory_path) if "packetfilter-" in file])

# 파일들에 대해 작업 수행
for raw_data_file in file_list:
    # 파일 이름에 따라 결과 파일 이름 설정
    output_file = os.path.join(directory_path, raw_data_file.replace('_modified_data.xlsx', '_final_data.xlsx'))

    # 데이터 불러오기
    df = pd.read_excel(os.path.join(directory_path, raw_data_file))

    # 각 값이 위치해야 할 열 인덱스
    correct_column_indices = {
        'action': 1,  # B열
        'initf': 2,   # C열
        'outitf': 3,  # D열
        'srcmac': 4,
        'dstmac': 5,
        'srcip': 6,   # G열
        'dstip': 7,   # H열
        'srcport': 8, # I열
        'dstport': 9  # J열
    }

    # 각 행을 순회하면서 데이터 재배치
    for index, row in df.iterrows():
        # B열부터 J열까지의 데이터를 변수에 저장
        row_data = row.iloc[1:10].tolist()

        # 저장된 데이터를 검사하여 올바른 열에 입력
        for data in row_data:
            if pd.notna(data):
                for key, col_index in correct_column_indices.items():
                    if key in str(data):
                        df.iat[index, col_index] = data
                        break

        # 각 열에서 정해진 값이 존재하지 않으면 빈칸으로 설정
        for key, col_index in correct_column_indices.items():
            column_value = str(df.iat[index, col_index])
            if not any(key in str(data) for data in row_data):
                df.iat[index, col_index] = None

    # 결과 저장
    df.to_excel(output_file, index=False)

    print(f"File '{raw_data_file}' processed and saved as '{output_file}'")
