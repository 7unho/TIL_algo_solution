"""
n := 격자 범위, 홀수
answer := 격자 바깥으로 나간 먼지의 양

a : 다른 격자에 이동한 먼지의 양 - 이동한 위치에 있던 먼지의 양
"""
n = int(input())
depth = n // 2 + 1
graph = [list(map(int, input().split())) for _ in range(n)]
# 서, 남, 동, 북
dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))
x, y = n // 2, n // 2
scatters = [
    [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (1, 1, 0.01),
     (-1, 1, 0.01)],
    [(2, 0, 0.05), (1, -1, 0.1), (1, 1, 0.1), (0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), (0, -1, 0.07), (-1, 1, 0.01),
     (-1, -1, 0.01)],
    [(0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (-2, 0, 0.02), (2, 0, 0.02), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.01),
     (1, -1, 0.01)],
    [(-2, 0, 0.05), (-1, -1, 0.1), (-1, 1, 0.1), (0, 2, 0.02), (0, -2, 0.02), (0, 1, 0.07), (0, -1, 0.07), (1, 1, 0.01),
     (1, -1, 0.01)]
]
answer = 0

def outOfRange(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def snail_pattern(max_depth):
    pattern = []
    for depth in range(1, max_depth + 1):
        directions = [0, 1, 2, 2, 3, 3]
        for dir in directions:
            if dir in (0, 1):
                pattern.extend([dir] * (2 * depth - 1))
            else:
                pattern.extend([dir] * depth)
    return pattern

def cleanUp(x, y, dir):
    global answer
    amount = graph[x][y]

    for dx, dy, percentage in scatters[dir]:
        dust = int(amount * percentage)
        nx, ny = x + dx, y + dy
        
        graph[x][y] -= dust
        if outOfRange(nx, ny):
            answer += dust
            continue
        graph[nx][ny] += dust
      
    nx, ny = x + dirs[dir][0], y + dirs[dir][1]
    if outOfRange(nx, ny): 
        answer += graph[x][y]
        graph[x][y] = 0
        return

    graph[nx][ny] += graph[x][y]
    graph[x][y] = 0


directions = snail_pattern(depth)

x, y = n // 2, n // 2
for dir in directions:
    nx, ny = x + dirs[dir][0], y + dirs[dir][1]
    if (nx, ny) == (0, -1): break

    cleanUp(nx, ny, dir)
    
    x, y = nx, ny

print(answer)