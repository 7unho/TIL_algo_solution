# 떡볶이 떡 만들기
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

start = 0
end = max(array)

result = 0

while start <= end:
    total = 0

    mid = (start + end) // 2

    for x in array:
        total += (x - mid) if x > mid else 0

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)