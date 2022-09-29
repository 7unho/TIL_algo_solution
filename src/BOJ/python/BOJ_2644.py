# 촌수 계산

from collections import deque
import sys
input = sys.stdin.readline
answer = 0

def bfs(x):
    while queue:
        x = queue.popleft()

        for nx in graph[x]:
            if dist[nx] == 0:
                dist[nx] = dist[x] + 1
                queue.append(nx)


n = int(input())
graph = [[] for _ in range(n + 1)]
dist = [0] * (n + 1)

a, b = map(int, input().split())

for _ in range(int(input())):
    x, y = map(int, input().split())
    graph[x] += [y]
    graph[y] += [x]

queue = deque([])
queue.append(a)

bfs(a)

answer = dist[b] if dist[b] != 0 else -1
print(answer)
