"""
x -> x - 1, x + 1, 2 * x
x - 1, x + 1 => 1초
2 * x => 0초
"""
import heapq

n, k = map(int, input().split())
answer = 0
INF = int(1e9)
dp = [INF] * (100_001)
dp[n] = 0

q = list()
q.append((0, n))

while q:
    dist, x = heapq.heappop(q)

    if x == k:
        break

    dir = ((dist + 1, x + 1), (dist + 1, x - 1), (dist, 2 * x))
    for nDist, nx in dir:
        if nx < 0 or nx >= 100_001: continue
        if dp[nx] <= nDist: continue
        dp[nx] = nDist
        heapq.heappush(q, (nDist, nx))

print(dp[k])