from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

# def count_binary_search(array, target):
#     result = 0

#     left_index = bisect_left(array, target)
#     right_index = bisect_right(array, target)

#     for i in range(left_index, right_index + 1):
#         if array[i] == target:
#             result += 1
#             continue
    
#     return result

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return right_index - left_index

N, x = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

result = count_by_range(array, x, x)
# result = count_binary_search(array, x)

print(result if result != 0 else -1)