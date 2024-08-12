# 문제 링크 : https://acm.timus.ru/problem.aspx?space=1&num=2144

def read_boxes(n):
    """
    n은 읽어야 하는 상자의 수이다.

    입력에서 상자들을 읽고 상자들의 리스트를 반환한다.
    각 상자는 액션 피규어의 높이를 담은 리스트이다.
    """

    boxes = []
    for i in range(n):
        box = input().split()
        box.pop(0)
        for i in range(len(box)):
            box[i] = int(box[i])
        boxes.append(box)
    return boxes

def box_ok(box):
    """

    box는 해당 상자 내부의 액션 피규어들의 높이를 담은 리스트이다.

    True를 반환하면 상자 내 액션 피규어들의 높이의 순서가 작아지지 않는 것이고,
    False는 그렇지 않은 것이다.
    """
    for i in range(len(box)-1):
        if box[i] > box[i + 1]:
            return False
    return True

def all_boxes_ok(boxes):
    """

    boxes는 상자들의 리스트이다. 각 상자는 액션 피규어 높이들의 리스트이다.

    상자 내의 액션 피규어의 높이가 점점 작아지지 않는다면 True를 반환하고,
    그렇지 않으면 False를 반환한다.
    """
    for box in boxes:
        if not box_ok(box):
            return False
    return True

def boxes_endpoints(boxes):
    """

    boxes는 상자들의 리스트이다. 각 박스는 액션 피규어의 높이를 가진 리스트이다.

    각각 두 개의 값이 있는 리스트들을 값으로 갖는 리스트를 반환한다.
    두 개의 값은 상자의 가장 왼쪽과 가장 오른쪽 액션 피규어의 높이이다.
    """

    endpoints = []
    for box in boxes:
        endpoints.append([box[0], box[-1]])
    return endpoints

def all_endpoints_ok(endpoints):
    """
    endpoints는 두 개의 값을 가진 리스트를 각 값으로 가진 리스트이다.
    두 개의 값은 상자의 가장 왼쪽과 오른쪽 액션 피규어의 높이이다.

    요구사항 : endpoints는 피규어의 높이로 정렬되어 있어야 한다.

    endpoints가 순서대로 정리가 가능한 상자들이라면 True를 반환하고,
    그렇지 않으면 False를 반환한다.
    """

    maximum = endpoints[0][1]
    for i in range(1, len(endpoints)):
        if endpoints[i][0] < maximum:
            return False
        maximum = endpoints[i][1]
    return True

# Main Program

# 입력을 읽는다.
n= int(input())
boxes = read_boxes(n)

# 모든 상자가 정상인지 확인한다.
if not all_boxes_ok(boxes):
    print('NO')
else:
    # 각 상자의 양 끝에 있는 액션 피규어 높이로 구성된 새로운 상자 리스트를 얻는다.
    endpoints = boxes_endpoints(boxes)

    # 새로운 상자들을 정렬한다.
    endpoints.sort()

    # 정렬된 상자들을 정리할 수 있는지 결정한다.
    if all_endpoints_ok(endpoints):
        print('YES')
    else:
        print('NO')

