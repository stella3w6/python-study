# 파일 링크 : https://usaco.org/index.php?page=viewproblem2&cpid=711

# 파일 읽기 및 쓰기
input_file = open('crossroad.in', 'r')
output_file = open('crossroad.out', 'w')

# 첫 번째 줄 : 관찰 횟수 N
N = int(input_file.readline().strip())

# 소의 마지막 위치를 저장할 배열(0~9 인덱스는 1~10 소에 해당)
last_position = [-1] * 10 # -1로 초기화하여 첫 관찰 시 비교를 쉽게 함

# 확정된 횡단 횟수
crossings = 0

# 각 관찰을 처리
for i in range(N):
    # 관찰 데이터를 공백 기준으로 나누고, 이를 정수형으로 변환
    observation = input_file.readline().strip().split()
    cow_id = int(observation[0])
    position = int(observation[1])

    # 배열의 cow_id -1 위치에 소의 마지막 위치를 기록
    if last_position[cow_id -1] == -1:
        # 첫 관찰이면 현재 위치 기록
        last_position[cow_id -1] = position
    elif last_position[cow_id -1] !=position:
        # 마지막 위치와 현재 위치가 다르면 횡단 증가
        crossings = crossings + 1
        last_position[cow_id -1] = position

# 결과 출력
output_file.write(f"{crossings}\n")

# 파일 닫기
input_file.close()
output_file.close()
