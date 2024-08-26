n = 0
k = 0
words = []
with open("word.in", "r") as scrHandle:
    data = []
    for line in scrHandle:
        data.append(line.strip().split(" "))
    if len(data) != 2: exit("invalid input")
    if len(data[0]) != 2: exit("invalid input")
    n = checkNumber(data[0][0], 1, 100)
    k = checkNumber(data[0][1], 1, 80)
    if len(data[1]) != n: exit("invalid input")
    words = data[1]

lines = []
line = ""
i = 0
for word in words:
    if len(line) - i + len(word) > k:
        lines.append(line.strip())
        line = ""
        line = line + word + " "
        i = i + 1

with open("word.out", "w") as dstHandle:
    for line in lines:
        dstHandle.write(line + "\n")
