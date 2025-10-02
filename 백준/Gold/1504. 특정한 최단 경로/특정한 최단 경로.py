"""
1번 노드에서 N번 노드까지의 최단 거리
"""
import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def solution(start):
    # start -> N까지의 최단거리 테이블
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        current, x = heapq.heappop(q)

        for nx, weight in graph[x]:
            nDist = current + weight

            if dist[nx] < nDist: continue
            dist[nx] = nDist
            heapq.heappush(q, (nDist, nx))

    return dist

# 필수 방문 노드
ea, eb = map(int, input().split())
a = solution(1)
b = solution(ea)
c = solution(eb)

# 1 -> ea -> eb -> N, 1 -> eb -> ea -> N
answer = min(a[ea] + b[eb] + c[N], a[eb] + c[ea] + b[N])
print(-1 if answer >= INF else answer)