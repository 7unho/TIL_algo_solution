"""
n := 격자의 범위
q := 회전 횟수
l := q만큼의 회전 레벨
"""

depth, q = map(int, input().split())
n = 2 ** depth
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
levels = list(map(int, input().split()))
answer = 0

def outOfRange(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def counting(graph):
    count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1

    return count

def rotate(sx, sy, ex, ey, origin):
    graph = [[0] * n for _ in range(n)]
    print(sx, sy, ex, ey)
    groups = [
        [sx, sy, ex // 2, ey // 2],
        [sx, ey // 2 + 1, ex // 2, ey],
        [ex // 2 + 1, sy, ex, ey // 2],
        [ex // 2 + 1, ey // 2 + 1, ex, ey]
    ]

    print(groups)

    return 0

def grouping(level, n):
    groups = []

    for i in range(0, n, 2 * level):
        sx, ex = i, 2 ** level - 1 + i
        for j in range(0, n, 2 * level):
            sy, ey = j, 2 ** level - 1 + j

            groups.append([sx, sy, ex, ey])

    return groups

def dfs(x, y):
    if outOfRange(x, y): return False
    if graph[x][y] == 0: return False
    if visited[x][y]: return False
    visited[x][y] = True
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True

for level in levels:
    # 1. level에 따른 범위 그룹 (sx, sy, ex, ey
    if level <= depth:
        groups = grouping(level, n)
        # # 2. 해당 범위 rotate
        for sx, sy, ex, ey in groups:
            rotated = rotate(sx, sy, ex, ey, graph)

        graph = rotated




# 2. 군집 개수
for i in range(n):
    for j in range(n):
        visited = [[False] * n for _ in range(n)]
        if dfs(i, j):
            answer = max(answer, counting(visited))

print(answer)

