import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return 1 if right_index - left_index > 0 else 0

N = int(input())
n_list = list(map(int, input().rstrip().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().rstrip().split()))

for target in m_list:
    print(count_by_range(n_list, target, target))
