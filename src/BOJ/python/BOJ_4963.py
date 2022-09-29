#섬의 개수, 대각선까지 검사
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
answer = []

def dfs(x, y):
    if x < 0 or y < 0 or x >= h or y >= w:
        return False
    if graph[x][y]:
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x + 1, y + 1)
        return True
    return False

while True:
    w, h = map(int, input().split())
    if h == 0 and w == 0:
        break

    graph = []
    result = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                result += 1

    answer.append(result)

for i in answer:
    print(i)