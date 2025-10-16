"""
A -> B 까지의 최소 비용과 경로
"""
import heapq

n = int(input())
m = int(input())
INF = int(1e9)

graph = [[] for _ in range(n)]
from_info = [-1] * n
dp = [INF] * n

for _ in range(m):
    a, b, dist = map(int, input().split())
    graph[a - 1].append([dist, b - 1])

start, end = map(lambda x: int(x) - 1, input().split())

q = list()
heapq.heappush(q, (0, start))
dp[start] = 0
points = list()

while q:
    dist, current = heapq.heappop(q)

    if current == end:
        points.append(end + 1)

        _from = end

        while _from != start:
            _from = from_info[_from]
            points.append(_from + 1)

        break


    for weight, next in graph[current]:
        cost = dist + weight

        if cost >= dp[next]: continue
        dp[next] = cost
        from_info[next] = current
        heapq.heappush(q, (cost, next))

print(dp[end])
print(len(points))
for point in points[::-1]:
    print(point, end=" ")