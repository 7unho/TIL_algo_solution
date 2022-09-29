import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
answers = list()

while True:
    N = int(input())
    tc = 1
    if N == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[INF] * (N) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dp[0][0] = graph[0][0]
    queue = list()
    heapq.heappush(queue, (0, 0, dp[0][0]))
    while queue:
        x, y, dist = heapq.heappop(queue)
        if dp[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            cost = dist + graph[nx][ny]
            if cost < dp[nx][ny]:
                dp[nx][ny] = cost
                heapq.heappush(queue, (nx, ny, cost))


    answers.append(dp[N - 1][N - 1])


for tc in range(len(answers)):
    print(f"Problem {tc + 1}: {answers[tc]}")
