import sys
input = sys.stdin.readline

def binary_search(array, target, start, end):
    if start > end:
        return False
    
    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)


N = int(input())
array = list(map(int, input().rstrip().split()))
array.sort()

M = int(input())
target = list(map(int, input().rstrip().split()))

for target_num in target:
    if binary_search(array, target_num, 0, N - 1):
        print('yes', end=' ')
        continue
    print('no', end=' ')

## 계수정렬 풀이

# n = int(input())
# array = [0] * 1000001

# for i in input().split():
#     array[int(i)] += 1

# m = int(input())
# targets = list(map(int, input().split()))

# for target in targets:
#     if array[target]:
#         print('yes', end=' ')
#         continue
#     print('no', end=' ')
