from collections import deque
def solution(n, edge):
    INF = int(1e9)
    answer = 0
    visited = [INF for _ in range(n)]
    graph = [[] for _ in range(n)]
    
    for s, e in edge:
        graph[s - 1].append(e - 1)
        graph[e - 1].append(s - 1)
        
    q = deque([])
    q.append([0, 0])
    visited[0] = 0
    while q:
        x, dist = q.popleft()
        
        for nx in graph[x]:
            if visited[nx] != INF: continue
            visited[nx] = dist + 1
            q.append([nx, dist + 1])
    
    return visited.count(max(visited))