import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
dp = list()

for i in range(N):
    dp.append([item if item == 1 else INF for item in graph[i]])

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

for i in range(N):
    for j in range(N):
        print(1 if dp[i][j] != INF else 0, end=" ")
    print()