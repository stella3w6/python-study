open('word.in', 'w').close()
open('word.in', 'r')

input_file = open('word.in', 'r')
for line in input_file:
    print(line.rstrip())

