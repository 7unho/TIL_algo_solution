# bisect_left(a, x) : 정렬된 순서를 유지하면서 a에 x를 삽입할 가장 왼쪽 인덱스를 리턴
# bisect_right(a, y): 정렬된 순서를 유지하면서 a에 y를 삽입할 가장 오른쪽 인덱스를 리턴

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 7]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))


## 값이 특정 범위에 속하는 데이터 개수 구하기
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))

print(count_by_range(a, -1, 3))