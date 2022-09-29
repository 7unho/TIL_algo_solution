# 숫자 카드
## 입력값 : m 개의 수를 입력받아 상근이가 가지고 있으면 1 아니면 0

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def binary_search(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return right_index - left_index

m = int(input())
m_array = list(map(int, input().split()))
m_array.sort()

n = int(input())
n_array = list(map(int, input().split()))

for item in n_array:
    result = binary_search(m_array, item, item)
    print(result, end=' ')