from collections import deque
# 동, 서, 남, 북
# answer = 최단거리 else -1
# 길 : 1, 벽 : 0
N, M = 0, 0
visited = []

def printMap(maps):
    for i in range(len(maps)):
        print(maps[i])

def solution(maps):
    global N, M, visited
    N, M = len(maps), len(maps[0])
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    
    q = deque()
    q.append((0, 0, 1))
    
    while q:
        x, y, dist = q.popleft()
        visited[x][y] = dist
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny] >= 0 or maps[nx][ny] == 0: continue
            visited[nx][ny] = dist + 1
            q.append((nx, ny, dist + 1))
    
    return visited[N - 1][M -1]