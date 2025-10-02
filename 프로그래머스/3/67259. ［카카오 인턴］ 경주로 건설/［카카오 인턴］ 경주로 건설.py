"""
N := 격자 크기
0 := 빈 칸
1 := 벽

start -> (0, 0)
직선 cost : 100
코너 cost : 500

answer = 0, 0 -> n - 1, n - 1 까지 이동하게 하는 견적서의 최소 비용
상하, 좌우
"""
import heapq

INF = int(1e9)
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

def outOfRange(x, y, n):
    return x < 0 or y < 0 or x >= n or y >= n

def solution(board):
    N = len(board)
    visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    q = list()

    for dir in [1, 2]:
        visited[0][0][dir] = 0
        heapq.heappush(q, (0, 0, 0, dir))

    while q:
        cost, x, y, dir = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            return cost

        for nDir, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            nCost = cost + 100 if dir == nDir else cost + 600

            if outOfRange(nx, ny, N): continue
            if board[nx][ny] == 1: continue
            if visited[nx][ny][dir] < nCost: continue
            
            visited[nx][ny][dir] = nCost
            heapq.heappush(q, (nCost, nx, ny, nDir))