import sys
from collections import deque
input = sys.stdin.readline


# N, M크기의 격자
# 1. 테두리의 격자는 2면 이상이 외부와 닿으면 녹는다.
# 1-1. 내부의 공간은 접촉으로 치지 않는다.

# 출력값 : 모눈종이가 모두 사라지는 시간

N, M = map(int, input().split(' '))

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque([])
    q.append([0, 0])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            
            # bfs 돌리는 데, 다음 좌표가 1보다 크거나 같다면 graph += 1
            if graph[nx][ny] >= 1:
                graph[nx][ny] += 1
            # 아니라면 방문체크 후 q에 append
            else:
                visited[nx][ny] = True
                q.append([nx, ny])

res = 0
while True:
    visited = [[False] * M for _ in range(N)]
    flag = 0

    bfs()

    # i ~ j, 
    for x in range(N):
        for y in range(M):
            # graph(x, y) >= 3이라면 0으로 바꿔주고 flag = 1
            if graph[x][y] >= 3:
                graph[x][y] = 0
                flag = 1
            
            # graph가 2리라면 1로 바꿔주기
            elif graph[x][y] == 2:
                graph[x][y] = 1
    
    # flag = 0이면 break
    if flag:
        res += 1
    else:
        break
    
print(res)