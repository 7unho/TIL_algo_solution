import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def bfs(x, y, limit):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if cpyGraph[x][y] >= limit:
        cpyGraph[x][y] = -1
        bfs(x + 1, y, limit)
        bfs(x - 1, y, limit)
        bfs(x, y + 1, limit)
        bfs(x, y - 1, limit)
        return True
    return False

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = []


minValue = min(map(min, graph))
maxValue = max(map(max, graph))

for h in range(minValue, maxValue):
    cpyGraph = [item[:] for item in graph]
    result = 0
    for i in range(n):
        for j in range(n):
            if bfs(i, j, h):
                result += 1
    answer.append(result)

print(max(answer))
