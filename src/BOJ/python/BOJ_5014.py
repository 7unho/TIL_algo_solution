# 스타트링크
## 입력값 : F, S, G, U, D ( F층의 건물, 현재 층, 타겟 층, UP버튼, DOWN버튼)

import sys
from collections import deque

def bfs(x):
    queue = deque([x])
    visited[x] = True

    while queue:
        x = queue.popleft()

        if x == G:
            return count[G]

        for i in range(2):
            nx = x + dx[i]
            if 0 < nx <= F and not visited[nx]:
                visited[nx] = 1
                count[nx] = count[x] + 1
                queue.append(nx)

    if count[G] == 0:
        return "use the stairs"

input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
dx = [U, -D]
visited = [0 for i in range(F+1)]
count = [0 for i in range(F+1)]
print(bfs(S))