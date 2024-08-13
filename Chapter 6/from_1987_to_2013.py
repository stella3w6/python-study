# 문제 링크 : https://dmoj.ca/problem/ccc13s1

def has_distinct_digits(year):
    """주어진 연도의 모든 자릿수가 서로 다른지 확인하는 함수"""
    digits = str(year)
    return len(set(digits)) == len(digits)

def next_year_with_distinct_digits(start_year):
    """주어진 연도 이후에 모든 자릿수가 서로 다른 연도를 찾는 함수"""
    year = start_year + 1
    while True:
        if has_distinct_digits(year):
            return year
        year = year + 1

# 입력 받기
Y = int(input().strip())

print(next_year_with_distinct_digits(Y))
