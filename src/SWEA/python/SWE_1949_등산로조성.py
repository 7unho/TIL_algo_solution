for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    answer = 0
    points = []
    MAX = 0

    dx = [0, 0, 1, 1]
    dy = [1, -1, 0, 0]

    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
        MAX = max(MAX, max(graph[i]))

    for i in range(N):
        for j in range(N):
            if graph[i][j] == MAX: points.append([i, j, 1])

    def dfs(point, visited, dist):
        global answer
        x = point[0]
        y = point[1]
        flag = point[2]
        answer = max(answer, dist)

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if visited[nx][ny]: continue
        
            if flag == 1 and graph[nx][ny] >= graph[x][y]:
                for i in range(1, K + 1):
                    graph[nx][ny] -= i
                    flag = 0
                    if graph[x][y] > graph[nx][ny]:
                        visited[nx][ny] = True
                        dfs([nx, ny, flag], visited, dist + 1)
                        visited[nx][ny] = False
                    flag = 1
                    graph[nx][ny] += i
            elif graph[nx][ny] < graph[x][y]:
                visited[nx][ny] = True
                dfs([nx, ny, flag], visited, dist + 1)
                visited[nx][ny] = False

    for point in points:
        visited = [[False] * N for _ in range(N)]
        dfs(point, visited, 1)

    print(f"#{tc} {answer}")

    # 무선, 원자, 벽돌, 보호필름
