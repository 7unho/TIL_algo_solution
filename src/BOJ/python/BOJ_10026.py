import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def dfs(x, y, color):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if cpyGraph[x][y] == color:
        cpyGraph[x][y] = -1
        dfs(x + 1, y, color)
        dfs(x - 1, y, color)
        dfs(x, y + 1, color)
        dfs(x, y - 1, color)
        return True
    return False


n = int(input())

graph = [list(map(int, input().rstrip().replace('R', '0')
                                       .replace('G', '1')
                                       .replace('B', '2'))) for _ in range(n)]

answer1, answer2 = 0, 0
answer = []
for color in range(3):
    result = 0
    cpyGraph = [item[:] for item in graph]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, color):
                result += 1
    answer.append(result)
answer1 = sum(answer)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            graph[i][j] = 1

answer = []
for color in range(1, 3):
    result = 0
    cpyGraph = [item[:] for item in graph]
    for i in range(n):
        for j in range(n):
            if dfs(i, j, color):
                result += 1
    answer.append(result)
answer2 = sum(answer)
print(f"{answer1} {answer2}")