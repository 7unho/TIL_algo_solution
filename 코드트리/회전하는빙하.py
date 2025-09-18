"""
n := 격자의 범위
q := 회전 횟수
l := q만큼의 회전 레벨
"""
import math

depth, q = map(int, input().split())
n = 2 ** depth
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
levels = list(map(int, input().split()))
totalCount = 0
cluster = 0
dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def outOfRange(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def counting(graph):
    count = 0

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                count += 1

    return count

def grouping(level, n, wx, wy):
    groups = []

    if n == 2:
        return [
            [wx, wy, wx, wy], 
            [wx, wy + 1, wx, wy + 1], 
            [wx + 1, wy, wx + 1, wy], 
            [wx + 1, wy + 1, wx + 1, wy + 1]
        ]

    for i in range(0, n, 2 ** level):
        sx, ex = i, 2 ** level - 1 + i
        for j in range(0, n, 2 ** level):
            sy, ey = j, 2 ** level - 1 + j

            groups.append([sx + wx, sy + wy, ex + wx, ey + wy])

    return groups

def rotate(sx, sy, ex, ey, origin):
    group_n = ex - sx + 1
    rKeys = {0:2, 1:0, 2:3, 3:1}

    # 각 그룹별 좌표 가중치 -> (0,0) 을 기준으로 groups의 좌표가 반환되므로, 원래 좌표를 구하기 위함
    groups = grouping(int(math.log2(group_n // 2)), group_n, sx, sy)
    database = []

    for gsx, gsy, gex, gey in groups:
        data = []
    
        for x in range(gsx, gex + 1):
            for y in range(gsy, gey + 1):
                data.append(origin[x][y])
        database.append(data)

    for i in range(4):
        data = database[rKeys[i]]
        index = 0
        
        gsx, gsy, gex, gey = groups[i]
        
        for x in range(gsx, gex + 1):
            for y in range(gsy, gey + 1):
                origin[x][y] = data[index]
                index += 1
    

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

def meltable(x, y):
    neighbors = 0
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if outOfRange(nx, ny): continue
        if graph[nx][ny] == 0: continue
        neighbors += 1

    return neighbors < 3

def melting(graph):
    melt_points = []

    for x in range(n):
        for y in range(n):
            if meltable(x, y):
                melt_points.append((x, y))

    for x, y in melt_points:
        graph[x][y] = max(0, graph[x][y] - 1)

for level in levels:
    # 1. level에 따른 범위 그룹 (sx, sy, ex, ey
    if level > 0 and level <= depth:
        level = min(level, depth)
        groups = grouping(level, n, 0, 0)

        # # 2. 해당 범위 rotate
        for group, (sx, sy, ex, ey) in enumerate(groups):
            rotate(sx, sy, ex, ey, graph)

    # 3. 빙하 녹이기
    melting(graph)


# 4. 전체 빙하 개수
for i in range(n):
    for j in range(n):
        totalCount += graph[i][j]

# 5. 군집 개수
for i in range(n):
    for j in range(n):
        visited = [[False] * n for _ in range(n)]
        if dfs(i, j):
            cluster = max(cluster, counting(visited))

print(totalCount)
print(cluster)

# 1 0 2 2 0 2 3 1 2 0 
