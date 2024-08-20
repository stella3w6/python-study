# 문제 링크 : https://usaco.org/index.php?page=viewproblem2&cpid=735

# 입력 파일 읽기
input_file = open('lostcow.in', 'r')
line = input_file.readline().split()
x = int(line[0])
y = int(line[1])
input_file.close()

# 농부 존의 위치 및 총 이동 거리 초기화
total_distance = 0
current_position = x

# 지그재그 패턴의 이동 거리 초기화
step_size = 1

# 반복문을 통해 농부 존이 소에게 도달할 때까지의 이동
while True:
    # 농부 존의 다음 목표 위치 계산(지그재그로 이동)
    next_position = x + step_size

    # 이동 거리를 계산할 때, 직접 비교하여 절대값 구하기
    if current_position <= y <= next_position or current_position >= y >= next_position:
        if y > current_position:
            total_distance = total_distance + y - current_position
        else:
            total_distance = total_distance + current_position - y
        break
    else:
        if next_position > current_position:
            total_distance = total_distance + next_position - current_position
        else:
            total_distance = total_distance + current_position - next_position

    # 현재 위치를 업데이트
    current_position = next_position

    # 다음 지그재그 이동 크기를 두 배로 증가 시키고 방향을 반대로 설정
    step_size = step_size * -2

# 출력 파일에 결과 쓰기
output_file = open('lostcow.out', 'w')
output_file.write(str(total_distance) + '\n')
output_file.close()


