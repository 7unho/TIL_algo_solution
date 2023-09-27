import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

answer = [[-1] * M for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def process(x, y):
    if x == N - 1 and y == M - 1: return 1
    
    if answer[x][y] == -1:
        answer[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            if graph[x][y] <= graph[nx][ny]: continue
            answer[x][y] += process(nx, ny)

    return answer[x][y]

print(process(0, 0))