n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if y <= -1 or y >= m or x <= -1 or x >= n:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j) :
            result += 1



print(result)
