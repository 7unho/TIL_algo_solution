N, M = map(int, input().split())
graph = []
MAX = 0
for i in range(N):
    graph.append(list(map(int, input().split())))
    MAX = max(MAX, max(graph[i]))

visited = [[False] * M for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
# DFS
## 가지 치기 : ans가 현재 만들 수 있는 최댓값보다 크다면
## 종료 조건 : depth == 3일 때,
def dfs(x, y, depth, sum):
    global answer

    if answer >= sum + (3 - depth) * MAX:
        return
    
    if depth == 3:
        answer = max(answer, sum)
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M or visited[nx][ny]:
            continue

        if depth == 1:
            visited[nx][ny] = True
            dfs(x, y, depth + 1, sum + graph[nx][ny])
            visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, sum + graph[nx][ny])
        visited[nx][ny] = False


for x in range(N):
    for y in range(M):
        visited[x][y] = True
        dfs(x, y, 0, graph[x][y])
        visited[x][y] = False
    
print(answer)