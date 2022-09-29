# 보급로
## 최단 경로 찾기 BFS

from collections import deque

def print_graph():
    for i in range(n):
        print(visited[i])

def bfs():
    global cnt
    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == n - 1:
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            visited[nx][ny] = min(visited[nx][ny], visited[x][y] + graph[nx][ny])
            
            queue.append((nx, ny))


for tc in range(int(input())):
    n = int(input())
    cnt = 0

    graph = [list(map(int, input())) for _ in range(n)]
    visited = [[10] * n for _ in range(n)]
    visited[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([])
    queue.append((0, 0))

    bfs()
    # print(f"#{tc + 1} {visited[n - 1][n - 1]}")

    print_graph()
    