from collections import deque

def bfs(start, n, graph):
    dists = [-1 for _ in range(n)]
    dists[start] = 0
    
    q = deque([start])
    
    while q:
        x = q.popleft()
        
        for next in graph[x]:
            if dists[next] != -1: continue
            dists[next] = dists[x] + 1
            q.append(next)
    
    return dists

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n)]
    
    for a, b in roads:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    
    dists = bfs(destination - 1, n, graph)
    
    for source in sources:
        answer.append(dists[source - 1])
    
    return answer