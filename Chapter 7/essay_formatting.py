# 파일 링크 : https://usaco.org/index.php?page=viewproblem2&cpid=987

# 파일 열기
input_file = open('word.in', 'r')
output_file = open('word.out', 'w')

# 첫 줄에서 N과 K 값을 읽어옴
lst = input_file.readline().split()
N = int(lst[0]) # 단어의 개수
K = int(lst[1]) # 각 줄의 최대 글자 수

# 두 번째 줄에서 단어들을 읽어옴
words = input_file.readline().split()

# 초기화
line = ''
chars_on_line = 0

# 모든 단어에 대한 반복
for word in words:
    # 단어가 현재 줄에 들어갈 수 있는지 확인
    if chars_on_line + len(word) <= K:
        # 현재 줄에 단어를 추가
        if chars_on_line > 0: # 줄 시작이 아니면 공백 추가
            line = line + ' '
            chars_on_line = chars_on_line + 1
        line = line + word
        chars_on_line = chars_on_line + len(word)
    else:
        # 현재 줄이 꽉 찼으면 출력 파일에 쓰고 새로운 줄 시작
        output_file.write(line + '\n')
        line = word
        chars_on_line = len(word)

# 마지막 줄 출력
if line:
    output_file.write(line + '\n')

# 파일 닫기
input_file.close()
output_file.close()

