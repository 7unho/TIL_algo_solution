"""
획득 가능한 아이템 최대 개수
n := 지역
m := 수색범위
r := 양방향 엣지 개수
"""
import heapq
INF = int(1e9)
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n)]
answer = 0

def search(start):
    result = items[start]
    dp = [INF] * n
    q = list()
    heapq.heappush(q, (0, start))

    while q:
        dist, current = heapq.heappop(q)

        for next, cost in graph[current]:
            nDist = dist + cost
            if nDist > m: continue
            if nDist >= dp[next]: continue
            dp[next] = nDist
            heapq.heappush(q, (dist + cost, next))

    for node in range(n):
        if node == start: continue
        if dp[node] == INF: continue
        result += items[node]

    return result

for _ in range(r):
    a, b, dist = map(int, input().split())
    graph[a - 1].append((b - 1, dist))
    graph[b - 1].append((a - 1, dist))

for node in range(n):
    answer = max(answer, search(node))

print(answer)