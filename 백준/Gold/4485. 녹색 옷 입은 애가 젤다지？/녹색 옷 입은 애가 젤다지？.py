import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

TC = 1
while True:
    N = int(input())

    if N == 0: break

    graph = [list(map(int, input().split())) for _ in range(N)]
    dp = [[INF] * N for _ in range(N)]


    dp[0][0] = graph[0][0]

    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))

    while q:
        dist, cur = heapq.heappop(q)
        x, y = cur

        if dist > dp[x][y]: continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue

            cost = dist + graph[nx][ny]

            if cost < dp[nx][ny]:
                dp[nx][ny] = cost
                heapq.heappush(q, (cost, (nx, ny)))

    print(f"Problem {TC}: {dp[N - 1][N - 1]}")
    TC += 1