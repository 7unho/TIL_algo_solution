import sys
input = sys.stdin.readline

# 입력값 : N(행), M(열), R(회전 수)
X, Y = 0, 1
N, M, R = map(int, input().split())
depth = min(N, M) // 2
graph = [list(map(int, input().split())) for _ in range(N)]


def rotate(start, end):
    global graph
    temp = graph[start[X]][start[Y]]
    
    # ⬅️ 방향
    for i in range(start[Y], end[Y]):
        graph[start[X]][i] = graph[start[X]][i + 1]

    # ⬆️ 방향
    for i in range(start[X], end[X]):
        graph[i][end[Y]] = graph[i + 1][end[Y]]
    
    # ➡️ 방향
    for i in range(end[Y], start[Y], -1):
        graph[end[X]][i] = graph[end[X]][i - 1]
    
    # ⬇️ 방향
    for i in range(end[X], start[X] + 1, -1):
        graph[i][start[Y]] = graph[i - 1][start[Y]]
    
    graph[start[X] + 1][start[Y]] = temp

for _ in range(R):
    for i in range(depth):
        rotate((0 + i, 0 + i), (N - 1 - i, M - 1 - i))

for i in range(N):
    print(*graph[i])
    