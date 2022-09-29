# 빙산

def check_graph():
    for i in range(n):
        if graph[i].count(0) < m:
            return False
    return True

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 1 or ny < 1 or nx >= n - 1 or ny >= m - 1:
                continue

            if not visited[nx][ny] and graph[nx][ny] != 0:
                visited[nx][ny] = True
                bfs_graph[nx][ny] = 0
                queue.append([nx, ny])

from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = 0

while True:
    if check_graph():
        answer = 0
        break

    bfs_graph = deepcopy(graph)
    melt_graph = deepcopy(graph)
    visited = [[False] * m for _ in range(n)]
    ice_grp = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if not visited[i][j] and graph[i][j] > 0:
                visited[i][j] = True
                queue = deque()
                queue.append([i, j])
                bfs()
                ice_grp += 1

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if melt_graph[i][j] == 0:
                    continue

                if melt_graph[nx][ny] == 0:
                    graph[i][j] = graph[i][j] - 1 if graph[i][j] > 0 else 0
    if ice_grp > 1:
        break

    answer += 1
    
print(answer)