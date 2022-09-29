# 내리막길

def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    
    if not visited[x][y]:
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m) and (graph[x][y] > graph[nx][ny]):
                dp[nx][ny] = max(dp[nx][ny], dp[nx][ny] + 1)
                dfs(nx, ny)
        
    pass

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

dfs(0, 0)

for i in range(n):
    print(dp[i])