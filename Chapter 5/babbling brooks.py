# 문제 링크 : https://dmoj.ca/problem/ccc00s2

n = int(input())   # 초기 시내의 수 입력

streams = []

for i in range(n):
    streams.append(int(input()))

done = False   # 반복 루프 방지

while not done:
    command = int(input())
    if command == 77:
        done = True   # 루프 종료
    elif command == 99:    # 시내의 분기/ 다음 두 줄에서 분기할 시내 번호와 왼쪽 분기의 백분율을 입력 받음
        stream = int(input()) - 1     # 0부터 시작하는 인덱스를 만들기 위해 -1
        percentage = int(input())
        left = streams[stream] * percentage / 100
        right = streams[stream] - left
        streams = streams[:stream] + [left, right] + streams[stream+1:]
    elif command == 88:   # 시내의 합류
        stream = int(input()) - 1
        left = streams[stream]
        right = streams[stream + 1]
        streams = streams[:stream] + [left + right] + streams[stream+2:]

for i in range(len(streams)):
    streams[i] = str(round(streams[i]))      # 각 시내의 흐름을 반올림하여 문자열로 변환

output = ''
for amount in streams:
    output = output + amount + ' '

print(output[:-1])    # 마지막에 추가된 공백 제거