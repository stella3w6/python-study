grass = 0
cows = []
with open("revegetate.in", "r") as srcHandle:
    data = []
    for line in srcHandle: data.append(line.strip().split(" "))
    if len(data[0]) != 2: exit("invalid input")
    grass = checkNumber(data[0][0], 2, 100)
    cow = checkNumber(data[0][1], 1, 150)
    if len(data) != cow + 1: exit("invalid input")
    for v in data[1:]:
        if len(v) !=2: exit("invalid input")
        cows.append([checkNumber(v[0], 1, grass), checkNumber(v[1], 1, grass)])

    likeGrass = [[] for i in range(grass + 1)]

    for i in cows:
        if len(likeGrass[i[0]]) == 3 or len(likeGrass[i[1]]) == 3:
            exit(f"grass is already 3")
        likeGrass[i[0]].append(i)
        likeGrass[i[1]].append(i)
    [[],[[4,1],[2,1]], [[2,4],[2,1],[5,2], [[3,5], [5,2],[2,4],[4,1]]
    seeding = [0 for i in range(grass + 1)]

likeGrass = [[],[[4,1],[2,1]], [[2,4],[2,1],[5,2]], ...

for i in range(1, len(seeding)):
    seed = 1
    for cow in likeGrass[i]:
        if cow[0] < i and seeding[cow[0]] >= seed:
            seed = seeding[cow[0]] + 1
        if cow[1] < i and seeding[cow[1]] >= seed:
            seed = seeding[cow[1]] +1
        if seed > 4: exit("seed is over 4")
        seeding[i] = seed

with open("revegetate.out", "w") as dstHandle:
    for seed in seeding[1:]:
        dstHandle.write(str(seed))
