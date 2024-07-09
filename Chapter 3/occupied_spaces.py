n = input()
if not n.isdigit():
    exit()
n = int(n)
if not 0 <= n <= 100:
    exit()

yesterday = input()
today = input()

occupied = 0

for i in range(len(yesterday)):
    if yesterday[i] == 'C' and today[i] == 'C':
        occupied = occupied + 1

print(occupied)