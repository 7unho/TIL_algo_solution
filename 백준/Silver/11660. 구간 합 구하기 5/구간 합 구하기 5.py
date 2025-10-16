import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# (x, y)까지의 누적합 배열
dp = [[0] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        dp[x][y] = graph[x - 1][y - 1] + dp[x][y - 1] + dp[x - 1][y] - dp[x - 1][y - 1]

for _ in range(m):
    sx, sy, ex, ey = map(int, input().split())

    print(dp[ex][ey] - (dp[sx - 1][ey] + dp[ex][sy - 1] - dp[sx - 1][sy - 1]))