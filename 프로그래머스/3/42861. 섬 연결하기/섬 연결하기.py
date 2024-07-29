from collections import deque
def solution(n, costs):
    answer = int(1e9)
    costs.sort(key=lambda x:x[2])
    graph = [[] for _ in range(n)]
    answer = 0

    for a, b, cost in costs:
        if areNodesConnected(graph, a, b): continue
        
        graph[a].append(b)
        graph[b].append(a)
        answer += cost
    
    return answer

def areNodesConnected(graph, start, end):
    visited = [False] * len(graph)
        
    q = deque([start])
    
    while q:
        x = q.popleft()
        visited[x] = True
        
        if x == end: break

        for nx in graph[x]:
            if visited[nx]: continue
            visited[nx] = True
            q.append(nx)

    return visited[start] and visited[end]