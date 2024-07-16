T = int(input())
P = int(input())
R = int(input())

current_day = 0
total_infected = P

while total_infected <= T:
    P = P * R
    total_infected = total_infected + P
    current_day = current_day + 1

print(current_day)

