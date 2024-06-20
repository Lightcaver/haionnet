import os
import pandas as pd

# 디렉토리 경로 설정
directory_path = r'C:/Users/next_/Desktop/24.05/SG105_본사/방화벽'

# 해당 디렉토리 내의 파일 중 "packetfilter-"이 포함된 파일 목록 가져오기
file_list = [file for file in os.listdir(directory_path) if "packetfilter-" in file]

# 파일들에 대해 작업 수행
for raw_data_file in file_list:
    # 파일 이름에 따라 결과 파일 이름 설정
    output_file = os.path.join(directory_path, raw_data_file.replace('.xlsx', '_modified_data.xlsx'))

    # 필요한 열 인덱스
    columns_to_use = [0, 9, 11, 12, 13, 14, 15, 16, 22, 23]
    new_columns = ["시간", "정책", "In 인터페이스", "Out 인터페이스", "목적지 물리적 주소",
                   "목적지 물리적 주소", "출발지 아이피", "목적지 아이피", "출발지 포트", "목적지 포트"]

    # DataFrame으로 데이터 로드
    df = pd.read_excel(os.path.join(directory_path, raw_data_file))

    # 필요한 열만 유지
    df = df.iloc[:, columns_to_use]

    # 새로운 컬럼 이름 설정
    df.columns = new_columns

    # 결과 파일로 저장
    df.to_excel(output_file, index=False)

    print(f"File '{raw_data_file}' processed and saved as '{output_file}'")