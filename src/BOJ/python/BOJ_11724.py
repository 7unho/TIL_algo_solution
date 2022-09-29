import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


node, edge = map(int, input().split())

graph = [[] for i in range(node+1)]
visited = [False] * (node+1)

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0

for i in range(1,node+1):
    if not visited[i]:
        dfs(i)
        result += 1

print(result)