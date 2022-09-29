import sys
input = sys.stdin.readline

N, M = map(int, input().split())

array = list(map(int, input().rstrip().split()))

start, result = 0, 0
end = max(array)

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