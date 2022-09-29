# 맥주 마시면서 걸어가기


def bfs():
    queue = deque()
    queue.append(start)

    while queue:
        x, y = queue.popleft()

        if abs(x - target[0]) + abs(y - target[1]) <= 1000:
            return True
        
        for i in range(n):
            nx, ny = point[i]
            dist = abs(nx - x) + abs(ny - y)

            if not visited[i] and dist <= 1000:
                visited[i] = True
                queue.append([nx, ny])
    return False

import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    start = list(map(int, input().split()))
    point = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n
    target = list(map(int, input().split()))

    answer = bfs()
    answer = 'happy' if answer else 'sad'
    print(answer)