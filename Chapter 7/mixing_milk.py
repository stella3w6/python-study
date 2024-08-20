#문제 링크 : https://usaco.org/index.php?page=viewproblem2&cpid=855

# 파일 입출력을 위한 코드
input_file = open('mixmilk.in', 'r')
output_file = open('mixmilk.out', 'w')

# 첫 번째 버킷
line = input_file.readline().split()
c1 = int(line[0]) # 첫 번째 버킷의 용량
m1 = int(line[1]) # 첫 번째 버킷의 우유 양

# 두 번째 버킷
line = input_file.readline().split()
c2 = int(line[0]) # 두 번째 버킷의 용량
m2 = int(line[1]) # 두 번째 버킷의 우유 양

# 세 번째 버킷
line = input_file.readline().split()
c3 = int(line[0]) #세 번째 버킷의 용량
m3 = int(line[1]) #세 번째 버킷의 우유 양

# 100번의 주입 작업
for i in range(100):
    if i % 3 == 0: # 버킷 1 -> 버킷 2
        amount = min(m1, c2 - m2) # 버킷 1에서 버킷 2로 옮길 수 있는 최대 양
        m1 = m1 - amount
        m2 = m2 + amount
    elif i % 3 == 1: # 버킷 2 -> 버킷 3
        amount = min(m2, c3 - m3)
        m2 = m2 - amount
        m3 = m3 + amount
    else: # 버킷 3 -> 버킷 1
        amount = min(m3, c1 - m1)
        m3 = m3 - amount
        m1 = m1 + amount

# 최종 결과 출력
output_file.write(f"{m1}\n")
output_file.write(f"{m2}\n")
output_file.write(f"{m3}\n")

# 파일 닫기
input_file.close()
output_file.close()


