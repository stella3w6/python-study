# 문제 링크 : https://dmoj.ca/problem/ccc18j3

def distance_between(lst, i, j):
    """
    lst는 도시간 거리의 리스트이다.
    i 와 j는 도시의 인덱스를 나타내는 변수이다

    인덱스 i 도시와 인덱스 j 도시간 거리를 계산하여 반환하라
    """
    if i < j:
        city1= i
        city2 = j
    else:
        city1 = j
        city2 = i
    total = 0
    for k in range(city1, city2):
        total = total + lst[k]
    return total

lst = input().split()
for i in range(len(lst)):
    lst[i] = int(lst[i])

for i in range(len(lst) + 1):
    distances = []
    for j in range(len(lst) + 1):
        distances.append(str(distance_between(lst, i, j)))
    print(' '.join(distances))


