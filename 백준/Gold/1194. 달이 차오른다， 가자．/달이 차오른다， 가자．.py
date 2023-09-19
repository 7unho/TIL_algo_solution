# {
#     빈칸: '.',
#     벽: "#",
#     열쇠: 'a', ~ ,'f',
#     문: 'A', ~ ,'F',
#     현재 위치: '0',
#     출구: '1'
# }

# answer : 한번의 움직임이 수평이나 수직으로 한칸 이동하는 것일 때, 탈출까지의 최소 이동횟수
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [[[False] * 64 for _ in range(M)] for _ in range(N)]

start_x, start_y = 0, 0
for i in range(N):
    if '0' not in graph[i]: continue
    start_x, start_y = i, graph[i].index('0')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


q = deque([[start_x, start_y, 0, 0]])
visited[start_x][start_y][0] = True

while q:
    x, y, cnt, key = q.popleft()
    
    if graph[x][y] == '1':
        print(cnt)
        exit(0)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < M): continue
        if graph[nx][ny] == '#' or visited[nx][ny][key]: continue
        # 현재 노드가 소문자 알파벳이라면 ( 열쇠라면 )
        if graph[nx][ny] in ['a', 'b', 'c', 'd', 'e', 'f']:
            nKey = (1 << (ord(graph[nx][ny]) - 97)) | key
            if not visited[nx][ny][nKey]:
                visited[nx][ny][nKey] = True
                visited[nx][ny][key] = True
                q.append((nx, ny, cnt + 1, nKey))
        # 현재 노드가 대문자 알파벳이라면 ( 문이라면 )
        elif graph[nx][ny] in ['A', 'B', 'C', 'D', 'E', 'F']:
            checkDoor = (1 << (ord(graph[nx][ny]) - 65)) & key
            if checkDoor > 0:
                visited[nx][ny][key] = True
                q.append((nx, ny, cnt + 1, key))
        # 현재 노드가 빈 칸이라면('.')
        else:
            visited[nx][ny][key] = True
            q.append((nx, ny, cnt + 1, key))

print(-1)

