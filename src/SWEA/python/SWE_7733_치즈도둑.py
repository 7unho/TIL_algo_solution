import sys
input = sys.stdin.readline



dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for tc in range(1, int(input()) + 1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 0일 일 때도 생각. 덩어리는 1개부터
    answer = 1

    # 그래프 업데이트
    def updateGraph(day):
        global graph, N
        for i in range(N):
            for j in range(N):
                if graph[i][j] <= day: graph[i][j] = -1

    def dfs(x, y):
        global visited
        
        # 범위 체크
        if x < 0 or y < 0 or x >= N or y >= N:
            return False
        
        # graph[x][y] 0보다 크면서 방문하지 않았을 때, dfs 탐색
        if graph[x][y] > 0 and not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                dfs(nx, ny)
            return True
        return False


    for day in range(1, 101):
        updateGraph(day)
        visited = [[False] * N for _ in range(N)]
        cnt = 0

        for i in range(N):
            for j in range(N):
                if dfs(i, j):
                    cnt += 1
        
        answer = max(answer, cnt)

    print(f"#{tc} {answer}")





