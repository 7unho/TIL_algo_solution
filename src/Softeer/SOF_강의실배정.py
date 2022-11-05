import sys, heapq
input = sys.stdin.readline

N = int(input())
result = []

for _ in range(N):
    start, end = map(int, input().split())
    heapq.heappush(result, (end, start))

answer = 0
current = 0
while result:
    end, start = heapq.heappop(result)

    if current <= start:
        current = end
        answer += 1

print(answer)