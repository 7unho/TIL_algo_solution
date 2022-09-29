import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return right_index - left_index

N = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

M = int(input())
m_list = list(map(int, input().split()))

for target in m_list:
    print(count_by_range(n_list, target, target), end=' ')

# array = dict()
# key_list = []

# for i in range(N):
#     if n_list[i] in key_list:
#         array[n_list[i]] += 1
#         print(array[n_list[i]])
#     else:
#         key_list.append(n_list[i])
#         array[n_list[i]] = 1

# for target in m_list:
#     if target in key_list:
#         print(array[target], end=' ')
#         continue
#     print(0, end=' ')
