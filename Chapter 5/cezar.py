#문제 링크 : https://dmoj.ca/problem/coci17c1p1

card_by_values = [0,0,4,4,4,4,4,4,4,4,16,4]

n = int(input())

current_sum = 0

for i in range(n):
    card_value = int(input())
    current_sum += card_value
    card_by_values[card_value] = card_by_values[card_value] - 1

remaining_sum = 21 - current_sum

cards_greater_than_remaining = sum(card_by_values[remaining_sum+1:])
cards_less_or_equal_to_remaining = sum(card_by_values[:remaining_sum+1])

if cards_greater_than_remaining >= cards_less_or_equal_to_remaining:
    print("DOSTA")
else:
    print("VUCI")