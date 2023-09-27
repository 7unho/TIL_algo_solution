import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
items = set()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 1
def process(x, y):
    global answer

    q = set([(x, y, graph[x][y])])

    while q:
        x, y, items = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < N and 0 <= ny < M): continue
            if graph[nx][ny] in items: continue
            q.add((nx, ny, items + graph[nx][ny]))
            answer = max(answer, len(items) + 1)


process(0, 0)

print(answer)