"""
N := 격자 크기
M := 빨간 색을 제외한 폭탄 종류의 수
C := 한 라운드마다 없어지는 폭탄 개수
ANSWER := 라운드별 C*C의 합계
graph[x][y]: {
    -1: 검정 돌,
    0: 빨강 폭탄,
    1~M: 서로 다른 색의 폭탄
}

폭탄 묶음: (같은 색 폭탄 or 빨간색을 포함한 묶음) 돌 2개 이상 포함
아래 과정을 폭탄 묶음이 없을 때 까지 반복

1. 현재 격자에서 크기가 가장 큰 폭탄 묶음을 조회
우선순위
    1. 빨간색 폭탄이 가장 적게 포함된 것
    2. 기준점 중 행이 큰 폭탄
        기준점: 빨간색이 아닌 가장 폭탄 중, (-행, 열)
    3. 기준 점 중 열이 작은 폭탄 묶음
2. 1에서의 폭탄 묶음을 제거.
    - 폭탄 제거 이후에는 위에 있던 폭탄들이 빈곳으로 떨어짐, 돌은 떨어지지 않음
3. 반시계 방향으로 90 회전
4. 다시 중력 작용
"""
import heapq
from collections import deque

def graphInfo(graph):
    print('=' * 46)
    for i in range(len(graph)):
        print(graph[i])

dirs = [(1, 0), (0, -1), (0, 1), (-1, 0)]
RED, ROCK, EMPTY = 0, -1, -2
answer = 0
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def outOfRange(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

def bfs(x, y, color):
    q = deque([(x, y)])
    bombs = list([(-x, y)]) # not red and -행, 열, -color
    visited[x][y] = True
    red_count = 0

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if outOfRange(nx, ny): continue
            if graph[nx][ny] not in (RED, color): continue
            if (-nx, ny) in bombs: continue
            visited[nx][ny] = True
            red_count = red_count + 1 if graph[nx][ny] == RED else red_count
            heapq.heappush(bombs, (-nx, ny))
            q.append((nx, ny))

    return (red_count, bombs)

def explode(bombs, graph):
    """폭탄 묶음 제거"""
    global answer
    explode_count = 0

    for x, y in bombs[2]:
        graph[abs(x)][y] = EMPTY
        explode_count += 1

    answer += explode_count ** 2

def drop(graph):
    """중력 작용 열단위로 이동"""
    for y in range(n):
        for x in range(n - 2, -1, -1):
            if outOfRange(x, y): continue
            if graph[x][y] in (EMPTY, ROCK): continue
            sx = x
            
            while True:
                nx = sx + 1

                if nx == n: break
                if graph[nx][y] != EMPTY: break

                sx = nx

            if sx == x: continue

            graph[sx][y] = graph[x][y]
            graph[x][y] = EMPTY

def rotate(origin):
    n = len(origin)
    graph = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            graph[n - 1 - y][x] = origin[x][y]
    return graph

while True:
    visited = [[False] * n for _ in range(n)]
    bomb_list = list()
    # 1. 폭탄 묶음을 조회( 빨간색을 하나 포함한 묶음 )
    for x in range(n):
        for y in range(n):
            if graph[x][y] in (ROCK, EMPTY, RED): continue
            if visited[x][y]: continue
            red_count, bombs = bfs(x, y, graph[x][y])
            if len(bombs) <= 1: continue
            heapq.heappush(bomb_list, (-len(bombs), red_count, bombs))

    if not bomb_list: break
    # 2. 1의 폭탄 묶음음 중 가장 우선순위가 높은 묶음 제거
    explode(heapq.heappop(bomb_list), graph)
    # 3. 중력 작용
    drop(graph)
    # 4.왼쪽으로 90도 회전
    graph = rotate(graph)

    # 5.중력 작용
    drop(graph)

print(answer)
