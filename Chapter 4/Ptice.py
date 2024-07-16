#문제 링크 : https://dmoj.ca/problem/coci08c1p2

exam_questions = int(input())
if not 0 <= exam_questions <= 100:
    exit("범위를 벗어남(0 <= n <= 100)")

correct_answers = input().strip()

adrian_sequence = "ABC"
bruno_sequence = "BABC"
goran_sequence = "CCAABB"

adrian_count = 0
bruno_count = 0
goran_count = 0

for i in range(exam_questions):
    if correct_answers[i] == adrian_sequence[i % len(adrian_sequence)]:
        adrian_count += 1
    if correct_answers[i] == bruno_sequence[i % len(bruno_sequence)]:
        bruno_count  += 1
    if correct_answers[i] == goran_sequence[i % len(goran_sequence)]:
        goran_count += 1

most = adrian_count
if bruno_count > most:
    most = bruno_count
if goran_count > most:
    most = goran_count

print(most)

if adrian_count == most:
    print('Adrian')
if bruno_count == most:
    print('Bruno')
if goran_count == most:
    print('Goran')

