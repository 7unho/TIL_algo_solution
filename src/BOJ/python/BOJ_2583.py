# 영역 구하기
## 입력값 : n, m, k(개의 직사각형) 출력값 : 직사각형의 개수와 각 넓이

from copy import deepcopy
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

answers = []
sum = 0
for _ in range(k):
    points = list(map(int, input().split()))

    for i in range(points[0], points[2]):
        for j in range(points[1], points[3]):
            graph[i][j] += 1

def dfs(x, y):
    global sum

    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        sum += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            dfs(nx, ny)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            answers.append(sum)
            sum = 0

answers.sort()
print(len(answers))
for answer in answers:
    print(answer, end=' ')