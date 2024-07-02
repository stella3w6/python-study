k = input()
if not k.isdigit():
    exit()
k = int(k)
if not 1 <= k <= 45:
    exit()

a = 1
b = 0

for i in range(k):
    new_a = b
    new_b = a + b
    a = new_a
    b = new_b

print(a, b)


