from collections import deque

N, M = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(N)]
visited = [[[False] * 64 for _ in range(M)] for _ in range(N)]

print(graph)

dx = [0, 0, 1, 1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0': 
            start_x, start_y = i, j
        
queue = deque([])
queue.append((start_x, start_y, 0, 0))
visited[start_x][start_y][0] = True

while queue:
    x, y, cnt, key = queue.popleft()
    print(x, y, cnt, key)

    if graph[x][y] == '1':
        print(cnt)
        exit(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            continue

        if graph[nx][ny] == '#' or visited[nx][ny][key]:
            continue

        # 현재 노드가 소문자 알파벳이라면 ( 열쇠라면 )
        print(graph[nx][ny])
        if graph[nx][ny] in ['a', 'b', 'c', 'd', 'e', 'f']:
            nKey = (1 << (ord(graph[nx][ny]) - 97)) | key
            print(f"nKey -> {nKey}")
            if not visited[nx][ny][nKey]:
                visited[nx][ny][nKey] = True
                visited[nx][ny][key] = True
                queue.append((nx, ny, cnt + 1, nKey))

        # 현재 노드가 대문자 알파벳이라면 ( 문이라면 )
        elif graph[nx][ny] in ['A', 'B', 'C', 'D', 'E', 'F']:
            print(key, ord(graph[nx][ny]))
            checkDoor = (1 << (ord(graph[nx][ny]) - 65)) & key
            if checkDoor > 0:
                visited[nx][ny][key] = True
                queue.append((nx, ny, cnt + 1, key))
        # 현재 노드가 빈 칸이라면('.')
        else:
            visited[nx][ny][key] = True
            queue.append((nx, ny, cnt + 1, key))

print(-1)
# bfs 종료 조건
## 1. 가능한 모든 경로를 탐색 했거나
## 2. 탈출구( '1' )을 만났을 때
## key = 000001 ~ 111111
