"""
N개의 노드 중 X까지의 거리가 가장 큰 노드 번호
"""

import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
answer = -1

for _ in range(M):
    FROM, TO, cost = map(int, input().split())
    graph[FROM].append((TO, cost))

def solution(start, target):
    dist = [INF] * (N + 1)
    dist[start] = 0
    q = [(0, start)]

    while q:
        current, x = heapq.heappop(q)

        if target == x:
            break

        for nx, cost in graph[x]:
            nDist = current + cost
            if dist[nx] < nDist: continue
            dist[nx] = nDist
            heapq.heappush(q, (nDist, nx))

    return dist[target]

for node in range(1, N + 1):
    if node == X: continue

    nodeToX = solution(node, X)
    xToNode = solution(X, node)


    answer = max(answer, nodeToX + xToNode)

print(answer)