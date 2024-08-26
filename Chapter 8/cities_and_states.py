# 문제 링크 : https://usaco.org/index.php?page=viewproblem2&cpid=667

with open('citystate.in', 'r') as input_file, open('citystate.out', 'w') as output_file:
    n = int(input_file.readline())

    combo_to_num = {}

    for i in range(n):
        lst = input_file.readline().split()
        city = lst[0][:2]
        state = lst[1]
        if city != state:
            combo = city + state
            if not combo in combo_to_num:
                combo_to_num[combo] = 1
            else:
                combo_to_num[combo] = combo_to_num[combo] + 1

    total = 0

    for combo in combo_to_num:
        other_combo = combo[2:] + combo[:2]
        if other_combo in combo_to_num:
            total = total + combo_to_num[combo] * combo_to_num[other_combo]

    output_file.write(str(total // 2) + '\n')

