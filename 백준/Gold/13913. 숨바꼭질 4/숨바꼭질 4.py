"""
N, K = 수빈이 위치, 동생 위치

가장 빠른 시간
이동 경로

걷기 : X - 1 or x + 1
점프 : 2 * X
"""


import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [False for _ in range(100_001)]

q = deque()
q.append((N, 0, [N]))
visited[N] = True

if N > K:
    print(N - K)
    print(*[int(i) for i in range(N, K - 1, -1)])
    sys.exit(0)

while q:
    x, dist, routes = q.popleft()

    if x == K: 
        print(dist)
        print(*routes)
        break

    for dx in (-1, 1, x):
        nx = x + dx
        if nx < 0 or nx > 100_000 or visited[nx]: continue
        
        visited[nx] = True
        q.append((nx, dist + 1, routes + [nx]))