obeys = input()
n = input()
if not n.isdigit():
    exit()
n = int(n)
if not 1 <= n <= 100:
    exit()

obeyed = obeys
total_obeys = 1

for i in range(n):
    line = input()
    winner = line[0]
    loser = line[2]
    if obeys == loser:
        obeys = winner
        if not winner in obeyed:
            total_obeys += 1
            obeyed = obeyed + winner

print(obeys)
print(total_obeys)

