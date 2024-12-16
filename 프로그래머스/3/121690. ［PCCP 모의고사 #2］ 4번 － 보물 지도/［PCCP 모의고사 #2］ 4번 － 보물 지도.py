"""
BFS, 신발을 썼을 경우, 안썼을 경우로 나눠서
graph = [
    0: 일반
    -1:함정
    1: 골인
]
"""
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def pointIsInValid(n, m, nx, ny) -> bool:    
    return nx < 0 or ny < 0 or nx >= m or ny >= n

def solution(n, m, hole):
    answer = -1
    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[[False, False] for _ in range(n)] for _ in range(m)]
    
    q = deque([])
    q.append([0, 0, False, 0]) # x, y, isUsed, dist
    graph[m - 1][n - 1] = 1
    visited[0][0][0] = True

    for y, x in hole:
        graph[x - 1][y - 1] = -1
    
    while q:
        x, y, isUsed, dist = q.popleft()
        
        if graph[x][y] == 1:
            answer = dist
            break
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if pointIsInValid(n, m, nx, ny): continue
            # 1. 구덩이가 아닐 경우
            if graph[nx][ny] != -1:
                if visited[nx][ny][isUsed]: continue
                visited[nx][ny][isUsed] = True
                q.append([nx, ny, isUsed, dist + 1])

            if isUsed: continue
            
            nx2, ny2 = nx + dx[i], ny + dy[i]
            
            if pointIsInValid(n, m, nx2, ny2): continue
            if visited[nx2][ny2][1]: continue
            if graph[nx2][ny2] == -1: continue
            
            visited[nx2][ny2][1] = True
            q.append([nx2, ny2, True, dist + 1])
                
    return answer
