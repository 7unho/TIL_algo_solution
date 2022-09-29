import sys
input = sys.stdin.readline

itemList = []
cnt = 0
def dfs(x, y):
    global itemList

    if x < 0 or y < 0 or x >= r or y >= c:
        return False
    if graph[x][y] not in itemList:
        itemList.append(graph[x][y])
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        print(itemList)
        return len(itemList)
    return False

r, c = map(int, input().split())

graph =[list(map(str, input())) for _ in range(r)]
answer = []
for i in range(r):
    for j in range(c):
        cnt = dfs(i, j)
        if cnt:
            answer.append(cnt)


print(max(answer))