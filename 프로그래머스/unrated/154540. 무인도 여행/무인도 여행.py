from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    q = deque([])
    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        maps[i] = list(maps[i])
    
    for i in range(N):
        for j in range(M):
            _sum = 0
            if maps[i][j] == 'X': continue
            if visited[i][j]: continue
            
            q.append([i, j])
            visited[i][j] = True
            
            while q:
                x, y = q.pop()
                _sum += int(maps[x][y])
                
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    
                    if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                    if maps[nx][ny] == 'X': continue
                    if visited[nx][ny]: continue
                    
                    visited[nx][ny] = True
                    q.append([nx, ny])
            answer.append(_sum)
            
    answer = sorted(answer) if answer else [-1]
    return answer