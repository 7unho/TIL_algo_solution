# 테트로미노
N, M = map(int, input().split())
graph = list()
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
        # ㅜ 블럭을 위해 1칸 이동후 dfs 진행
        if depth == 1:
            visited[nx][ny] = True
            dfs(x, y, depth + 1, sum + graph[nx][ny])
            visited[nx][ny] = False
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, sum + graph[nx][ny])
        visited[nx][ny] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 0, graph[i][j])
        visited[i][j] = False

print(answer)
