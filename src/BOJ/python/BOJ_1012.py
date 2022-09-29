def dfs(x, y):
    if x <= -1 or y <= -1 or x >= n or y >= m:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False

t = int(input())
resList = []
for _ in range(t):
    n, m, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    result = 0

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1

    resList.append(result)

for item in resList:
    print(item)