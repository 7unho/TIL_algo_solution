# 벽 부수고 이동하기

from collections import deque
from copy import deepcopy
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

cnt_graph = [[[0] * 2 for _ in range(m)] for _ in range(n)]
cnt_graph[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = deque()
queue.append([0, 0, 0])

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1 and z == 0:
                cnt_graph[nx][ny][1] = cnt_graph[x][y][0] + 1
                queue.append([nx, ny, 1])
            elif graph[nx][ny] == 0 and cnt_graph[nx][ny][z] == 0:
                cnt_graph[nx][ny][z] = cnt_graph[x][y][z] + 1
                queue.append([nx, ny, z])

    return cnt_graph[n - 1][m - 1][z]

answer = bfs()
print(answer if answer != 0 else -1)

