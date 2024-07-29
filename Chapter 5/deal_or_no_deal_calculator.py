#문제 링크 : https://dmoj.ca/problem/ccc07j3

amounts = [0, 100, 500, 10000, 25000, 50000, 100000, 500000, 1000000]

n = int(input())

for i in range(n):
    used = int(input())
    amounts[used] = 0

total = 0
for amount in amounts:
    total = total + amount

average = total / (10 - n)

banker_offer = int(input())

if banker_offer > average:
    print('deal')
else:
    print('no deal')