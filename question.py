# 이진탐색

# 27. 정렬된 배열에서 특정 수의 개수 구하기
def count_specific_number(first: list, array: list) -> int:
    '''
    정렬된 배열에서 특정 수의 개수 구하기
    n개의 원소를 포함하는 오름차순 수열(array)
    x가 등장하는 회수 계산. 없으면 -1
    O(logN) 시간복잡도로 구현
    '''
    import bisect
    n, x = first
    if x not in array:
        return -1
    first_index = bisect.bisect_left(array, x)
    last_index = bisect.bisect_right(array, x)
    return (last_index - first_index) + 1


# 28. 고정점 찾기
def find_fixed_point(n: int, array: list) -> int:
    '''
    고정점: 수열의 원소 중에서 값이 인덱스와 동일한 원소

    수열 array는 총 n개의 원소를 포함함. (오름차순)
    수열에서 고정점이 있다면 이를 반환하고 아니면 -1을 반환 (고정점은 최대 1개)
    O(logN) 시간복잡도로 구현
    '''
    # for문으로 돌리면서 확인하면 시간복잡도에 걸리는듯
    # 오름차순이기 때문에 이진탐색을 통해서 문제풀이
    # 중간값이 index보다 작으면 오른쪽을,
    # 중간값이 index보다 크면 왼쪽을 탐색
    # 반복
    # 1. wile문으로 작성
    start_index = 0
    end_index = len(array) - 1
    while start_index <= end_index:
        # 중간값 찾기
        mid_index = (start_index + end_index) // 2
        # 중간값이 index와 같으면 고정점 반환
        if mid_index == array[mid_index]:
            return array[mid_index]
        # 중간값이 index보다 작으면
        if array[mid_index] < mid_index:
            # 오른쪽 탐색 (start는 end + 1)
            start_index = mid_index + 1
        # 중간값이 index보다 크면
        else:
            # 왼쪽 탐색 (end는 mid - 1)
            end_index = mid_index - 1
    return -1

# 28. 재귀문으로 풀이
def binary_search(array: list, start_index: int, end_index: int):
    if start_index > end_index:
        return -1
    mid_index = (start_index + end_index) // 2
    if array[mid_index] == mid_index:
        return array[mid_index]
    if array[mid_index] < mid_index:
        start_index = mid_index + 1
    else:
        end_index = mid_index - 1
    return binary_search(array, start_index, end_index)

def find_fixed_point_reculsive(n: int, array: list) -> int:
    return binary_search(array, 0, len(array) - 1)
