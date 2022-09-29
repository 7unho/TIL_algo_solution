# 토마토

## 보관 후 하루가 지나면 익은 토마토와 인접한 토마토가 익게된다.
## 며칠이 지나면 다 익게 되는지 최소 일수 출력
## 입력값 : n, m 출력값 : 최소 날짜, (저장될 때 부터 다 익어있는 상태 : 0 ( 그래프 안에 0이 없으면), 모두 익지 못하면 : -1 ( 그래프 안에 0이 있으면 ))
### 0 : 안익은 토마토, 1: 익은 토마토, -1: 빈 칸

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
zero_cnt = 0
graph = []
queue = deque([])
for i in range(m):
    graph.append(list(map(int, input().rstrip().split())))
    zero_cnt += graph[i].count(0)
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

if zero_cnt == 0:
    print(0)
else:
    bfs()
    zero_cnt, answer = 0, 0

    for i in range(m):
        zero_cnt += graph[i].count(0)
        answer = max(answer, max(graph[i]) - 1)
    
    answer = answer if zero_cnt == 0 else -1
    print(answer)


