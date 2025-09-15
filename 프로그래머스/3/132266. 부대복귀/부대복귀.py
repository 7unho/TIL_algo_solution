import heapq

INF = int(1e9)

def bfs(start, n, graph):
    global INF
    dists = [INF for _ in range(n)]
    dists[start] = 0
    
    q = list()
    heapq.heappush(q, (start, 0))
    
    while q:
        x, dist = heapq.heappop(q)
        
        if dists[x] < dist: continue
        
        for next in graph[x]:
            if dist + 1 >= dists[next]: continue
            dists[next] = dist + 1
            heapq.heappush(q, (next, dist + 1))
    
    return dists

def solution(n, roads, sources, destination):
    global INF
    answer = []
    
    graph = [[] for _ in range(n)]
    
    for a, b in roads:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
        
    dists = bfs(destination - 1, n, graph)
        
    for source in sources:
        answer.append(-1 if dists[source - 1] == INF else dists[source - 1])
    
    return answer