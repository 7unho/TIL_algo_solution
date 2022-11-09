import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    # N : N*N graph, K : 깎을 수 있는 높이.
    N, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    MAX = 0
    flag = 1
    answer = 0

    points = []

    # 최댓값 찾기
    for i in range(N):
        MAX = max(MAX, max(graph[i]))

    # 최댓값인 곳의 좌표 points에 추가
    for i in range(N):
        for j in range(N):
            if graph[i][j] == MAX: points.append((i, j))


    visited = [[False] * N for _ in range(N)]
    
    # 탐색.
    def dfs(x, y, dist):
        global answer, flag
        answer = max(answer, dist)


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
                continue

            # 횟수가 남아있으면서, 현재 높이보다 크거나 같다면.
            if flag == 1 and graph[nx][ny] >= graph[x][y]:
                # K 감소하면서 최댓값으로 깎아내리기..
                for depth in range(1, K + 1):
                    flag = 0
                    if graph[nx][ny] - depth < graph[x][y]:
                        visited[nx][ny] = True
                        graph[nx][ny] -= depth
                        dfs(nx, ny, dist + 1)
                        graph[nx][ny] += depth
                        visited[nx][ny] = False
                    flag = 1
            # 현재 높이보다 작다면
            elif graph[nx][ny] < graph[x][y]:
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False

    for x, y in points:
        # 시작 좌표 방문처리 제대로 해주기..!
        visited[x][y] = True
        dfs(x, y, 1)
        visited[x][y] = False

    print(f"#{tc} {answer}")
