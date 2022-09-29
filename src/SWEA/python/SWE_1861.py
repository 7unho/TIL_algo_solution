from importlib.machinery import FrozenImporter
import sys
input = sys.stdin.readline

answer = 0
answer_num = 1000000000

def dfs(x, y, cnt):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= N or ny >= N or nx < 0 or ny < 0:
            return False

        if graph[x][y] + 1 != graph[nx][ny]:
            return False

        dfs(nx, ny, cnt + 1)
        return cnt

graph = list()
for tc in range(1, int(input()) + 1):

    N = int(input())
    
    graph = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            answer = max(answer, dfs(i, j, 0))
            answer_num = min(answer_num, graph[i][j])

    print(answer_num, answer)