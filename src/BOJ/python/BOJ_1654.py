import sys
input = sys.stdin.readline

N, K = map(int, input().split())

array = []
for _ in range(N):
    array.append(int(input()))

start, result = 1, 0
end = max(array)

while start <= end:
    total = 0

    mid = (start + end) // 2

    for x in array:
        total += (x // mid)

    if total < K:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)