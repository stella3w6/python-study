# 문제 링크 : https://dmoj.ca/problem/ecoo19r2p1

def clean(address):
    """
    address는 이메일 주소를 나타내는 문자열입니다.

    정리된 이메일 주소를 반환합니다.
    """
    # + 기호와 @ 기호 사이의 모든 문자를 제거한다.
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]

    # @ 기호 앞에 있는 모든 점을 제거한다.
    at_index = address.find('@')
    before_at = ''
    i = 0
    while i < at_index:
        if address[i] != '.':
            before_at = before_at + address[i]
        i = i + 1

    cleaned = before_at + address[at_index:]

    # 소문자로 변환한다.
    cleaned = cleaned.lower()

    return cleaned


# Main Program

for dataset in range(10):
    n = int(input())
    addresses = set()
    for i in range(n):
        address = input()
        address = clean(address)
        addresses.add(address)

    print(len(addresses))
