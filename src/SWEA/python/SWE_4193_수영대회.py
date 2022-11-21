from collections import deque

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[-1] * N for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    q = deque([])

    q.append((start_x, start_y))
    dist[start_x][start_y] = 0
    cnt = 1

    def print_dist():
        for i in range(N):
            print(dist[i])


    def print_graph():
        for i in range(N):
            print(graph[i])


    while q:
        x, y = q.popleft()

        if (x, y) == (target_x, target_y):
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나거나 돌이라면
            if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] == 1:
                continue

            if graph[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

            # 소용돌이 일 때,
            if graph[nx][ny] == 2:
                graph[nx][ny] = 0
                dist[nx][ny] = dist[x][y] + 3 - dist[x][y] % 3
                q.append((nx, ny))
                continue
    print(f"#{tc} {dist[target_x][target_y]}")


