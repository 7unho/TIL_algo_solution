from collections import deque
from copy import deepcopy
n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def count_zero(x,y):
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<n and 0<=ny<m and data[nx][ny]==0:
            cnt += 1
    return cnt

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visit = [[0] * m for _ in range(n)]
    visit[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and visit[nx][ny]==0 and new_data[nx][ny]!=0:
                visit[nx][ny] = 1
                new_data[nx][ny] = 0
                q.append((nx,ny))

def check_melt():
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                return False
    return True

year = 0
while 1:
    year += 1
    if check_melt():
        print(0)
        break

    new_data = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if data[i][j] != 0:
                zero = count_zero(i,j)
                value = data[i][j] - zero
                new_data[i][j] = value if value >= 0 else 0
    data = deepcopy(new_data)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if new_data[i][j] != 0:
                bfs(i,j)
                cnt += 1
    if cnt >= 2:
        print(year)
        break