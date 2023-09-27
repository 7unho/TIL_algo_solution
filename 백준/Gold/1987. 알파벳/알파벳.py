import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
visited = [False] * 26
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 1
visited[ord(graph[0][0]) - 65] = True

def process(x, y, items):
    global answer

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < N and 0 <= ny < M): continue
        item = ord(graph[nx][ny]) - 65
        if visited[item]: continue
        visited[item] = True
        items.add(item)
        answer = max(answer, len(items))
        process(nx, ny, items)
        visited[item] = False
        items.remove(item)
        

process(0, 0, {ord(graph[0][0]) - 65})

print(answer)