from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m, v = map(int, input().split())

graph = [0]
visited = [False] * (n + 1)

for _ in range(n):
    graph.append([])

for _ in range(m):
    a, b = map(int, input().split())
    for i in range(1, n+1):
        if a == i:
            graph[i].append(b)
        if b == i:
            graph[i].append(a)
        graph[i].sort()

dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)
