from collections import deque
# X는 지나갈 수 없음.
# S, E, L(레버), O(통로)

# S -> L, L -> E
N = 0
M = 0
s, e, l = [-1, -1], [-1, -1], [-1, -1]
answer = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = []
def bfs(start, target, dist, maps):
    global N, M, visited
    
    q = deque([start + [dist]])
    
    while q:
        x, y, dist = q.popleft()
        visited[x][y] = True
        
        if [x, y] == target:
            return dist
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if visited[nx][ny]: continue
            if maps[nx][ny] == 'X': continue
            
            visited[nx][ny] = True
            q.append([nx, ny, dist + 1])
    return -1


def solution(maps):
    global N, M, s, e, l, answer, visited
    N = len(maps)
    M = len(maps[0])
    s, e, l = [-1, -1], [-1, -1], [-1, -1]
    answer = 0
        
    for i in range(N):
        maps[i] = list(maps[i])
        for j in range(M):
            if maps[i][j] == 'S':
                s = [i, j]
            elif maps[i][j] == 'E':
                e = [i, j]
            elif maps[i][j] == 'L':
                l = [i, j]
    
    # S -> L 까지의 거리
    visited = [[False] * M for _ in range(N)]
    start_to_lever = bfs(s, l, 0, maps)
   
    if start_to_lever == -1: return start_to_lever

    # L -> E 까지의 거리
    visited = [[False] * M for _ in range(N)]
    lever_to_end = bfs(l, e, 0, maps)
    
    return start_to_lever + lever_to_end if lever_to_end != -1 else lever_to_end











