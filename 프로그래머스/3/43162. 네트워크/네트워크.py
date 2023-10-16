graph = []
visited = []
def dfs(x, n):
    global visited, graph
    if x < 0 or x >= n: return False
    if visited[x]: return False
    visited[x] = True
    
    for nx in graph[x]:
        dfs(nx, n)
    
    return True

def init(n, computers):
    global graph
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if computers[i][j] == 0: continue
            graph[i].append(j)

def solution(n, computers):
    global graph, visited
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    init(n, computers)
    
    for node in range(n):
        if dfs(node, n): answer += 1
    return answer