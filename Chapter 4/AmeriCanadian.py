#문제 링크 : https://dmoj.ca/problem/ccc02j2

while True:
    word = input()
    if word == "quit!":
        break

    if len(word) > 4 and word[-2:] == "or" and word[-3] not in "aeiouy":
        print(word[:-2] + 'our')
    else:
        print(word)