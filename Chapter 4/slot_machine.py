chips = int(input())
first = int(input())
second = int(input())
third = int(input())

plays = 0

while chips >= 1:
    machine = plays % 3
    chips = chips - 1

    if machine == 0:
        first = first + 1
        if first % 35 == 0:
            chips = chips + 30
    elif machine == 1:
        second = second + 1
        if second % 100 == 0:
            chips = chips + 60
    elif machine == 2:
        third = third + 1
        if third % 10 == 0:
             chips = chips + 9

    plays = plays + 1

print(f'Martha plays {plays} times before going broke.')

#문제 링크 : https://dmoj.ca/problem/ccc00s1