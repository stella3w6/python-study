# 입력 파일을 열고 데이터 읽기
input_file = open("word.in", "r")

# 첫 번째 줄에서 n과 k를 읽는다.
n, k = map(int, input_file.readline().split())

# 두 번째 줄에서 n개의 단어를 읽어온다.
words = input_file.readline().split()

# 결과를 저장할 줄 리스트
lines = []
line = ""

# 파일 닫기
input_file.close()

# 단어를 한 줄씩 추가하면서 처리
for word in words:
    # 현재 줄에 단어를 추가했을 때, 그 줄이 k 문자를 넘는지 확인
    if len(line) + len(word) < k:
        # 공백이 있을 경우 추가 후 단어를 더함
        if line:
            line = line + " "
        line = line + word
    else:
        # 현재 줄이 꽉 찼다면 lines에 추가하고 새로운 줄로 초기화
        lines.append(line)
        line = word

# 마지막 줄 추가
if line:
    lines.append(line)

# 결과를 출력 파일에 쓴다
output_file = open("word.out", "w")
for line in lines:
    output_file.write(line + "\n")
output_file.close()