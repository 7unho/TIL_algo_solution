# 나이트의 이동
## 입력값: N * N 의 체스판, 나이트의 현재 칸, 나이트의 목표 칸

import sys
from collections import deque

input = sys.stdin.readline
answers = []

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    if x == target_x and y == target_y:
        answers.append(0)
        continue
    
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    queue = deque([(x, y)])

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n and 0 <= ny < n) and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    answers.append(graph[target_x][target_y])

for answer in answers:
    print(answer)