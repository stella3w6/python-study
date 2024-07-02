n = input()
if not n.isdigit():
    exit()
n = int(n)
if not 0 <= n <= 10000:
    exit()

student_answers = ''
for i in range(n):
    student_answers += input()

answer_key = ''
for i in range(n):
    answer_key += input()

correct_answers = 0
for i in range(n):
    if student_answers[i] == answer_key[i]:
        correct_answers += 1

print(correct_answers)






