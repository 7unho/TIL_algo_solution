# 1번 집의 색은 2번 집과 달라야 한다.
# N번 집의 색은 N - 1과 달라야 한다.
# i (2 ~ N - 1)의 집은 i - 1, i + 1과 달라야 한다.

import sys
input = sys.stdin.readline

N = int(input())
dp = [[0, 0, 0] for _ in range(N + 1)]

graph = [list(map(int, input().split())) for _ in range(N)]
graph.insert(0, [0, 0, 0])

dp[1] = graph[1][:]

for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + graph[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + graph[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + graph[i][2]

print(dp[N])