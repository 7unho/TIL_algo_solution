# N * M 맵에서 R,C에서 출발한 탈주범이 L초에 있을 수 있는 좌표의 수

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# case : 1 // 4 방위 -> i : 0, 1, 2, 3
# case : 2 // 상, 하 -> i : 0, 1
# case : 3 // 좌, 우 -> i : 2, 3
# case : 4 // 상, 우 -> i : 0, 3
# case : 5 // 하, 우 -> i : 1, 3
# case : 6 // 하, 좌 -> i : 1, 2
# case : 7 // 상, 좌 -> i : 0, 2

case = [[1, 2, 5, 6],
        [1, 2, 4, 7],
        [1, 3, 4, 5],
        [1, 3, 6, 7]]


def check(x, y, direction):
    if graph[x][y] == 1:
        if graph[nx][ny] in case[direction]:
            return True
    
    if graph[x][y] == 2 and direction in [0, 1]:
        if graph[nx][ny] in case[direction]:
            return True
    
    if graph[x][y] == 3 and direction in [2, 3]:
        if graph[nx][ny] in case[direction]:
            return True
    
    if graph[x][y] == 4 and direction in [0, 3]:
        if graph[nx][ny] in case[direction]:
            return True
    
    if graph[x][y] == 5 and direction in [1, 3]:
        if graph[nx][ny] in case[direction]:
            return True
    
    if graph[x][y] == 6 and direction in [1, 2]:
        if graph[nx][ny] in case[direction]:
            return True
    
    if graph[x][y] == 7 and direction in [0, 2]:
        if graph[nx][ny] in case[direction]:
            return True
    
    return False

for tc in range(int(input())):
    N, M, R, C, L = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    queue = deque([(R, C)])
    visited[R][C] = 1
    answer = 0

    while queue:
        x, y = queue.popleft()

        if visited[x][y] == L:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] == 0:
                continue

            if not check(x, y, i):
                continue

            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))


    for i in range(N):
        answer += (M - visited[i].count(0))

    print(f"#{tc + 1} {answer}")
