import csv

# 입력 파일과 출력 파일의 이름을 지정합니다.
input_file = 'experiment_btob.wav.csv'
output_file = 'experiment_btob_sm_detection.csv'

# 입력 파일을 읽고 처리하여 출력 파일로 저장합니다.
with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile, delimiter='\t')
    writer = csv.writer(outfile, delimiter='\t')

    for row in reader:
        # 각 행의 모든 요소에 대해 소수점 두 자리로 반올림합니다.
        rounded_row = [round(float(value), 2) if value.replace('.', '', 1).isdigit() else value for value in row]
        writer.writerow(rounded_row)

print(f"{input_file} 파일의 모든 숫자가 반올림되었습니다.")
