def dfs(x, y):
    global cnt
    if y <= -1 or y >= n or x <= -1 or x >= n:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return cnt
    return False

n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

cntList = []
total = 0
cnt = 0

for i in range(n):
    for j in range(n):
        cnt = dfs(i, j)
        if cnt :
            total += 1
            cntList.append(cnt)

print(total)
for item in sorted(cntList):
    print(item)

