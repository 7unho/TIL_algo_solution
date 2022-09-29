def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            dfs(graph, i, visited)


inputNode = int(input())
inputEdge = int(input())

graph = [0]
visited = [False] * (inputNode + 1)

for _ in range(inputNode):
    graph.append([])

for _ in range(inputEdge):
    a, b = map(int, input().split())
    for i in range(1, inputNode + 1):
        if a == i:
            graph[i].append(b)
        if b == i:
            graph[i].append(a)
        graph[i].sort()

dfs(graph, 1, visited)
print(visited.count(True) - 1)
