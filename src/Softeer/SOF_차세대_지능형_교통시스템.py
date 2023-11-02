"""
소프티어 LV3. 안전운전을 도와줄 차세대 지능형 교통시스템
https://softeer.ai/practice/6274

N := 그래프 크기
T := 시간

answer := 방문한 교차로 개수
"""
# == import 선언 부
from collections import deque
import sys
input = sys.stdin.readline

# == 변수 선언 부
N, T = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1)) # 상, 하, 좌, 우
UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
signals = [
     [],
     [RIGHT, [UP, RIGHT, DOWN]],
     [UP, [LEFT, UP, RIGHT]],
     [LEFT, [UP, LEFT, DOWN]],
     [DOWN, [DOWN, LEFT, RIGHT]],
     [RIGHT, [RIGHT, UP]],
     [UP, [UP, LEFT]],
     [LEFT, [LEFT, DOWN]],
     [DOWN, [DOWN, RIGHT]],
     [RIGHT, [RIGHT, DOWN]],
     [UP, [UP, RIGHT]],
     [LEFT, [LEFT, UP]],
     [DOWN, [DOWN, LEFT]]
]

# == process

q = deque()
q.append((0, 0, 0, UP)) # x, y, time, prev
answer = 0

while q:
    x, y, time, prev = q.popleft()
    if not visited[x][y]:
        visited[x][y] = True
        answer += 1
    # 시간이 다 되었다면
    if time == T: continue

    # 진입 방향과 신호등 방향 체크
    nPath = signals[graph[x][y][time % 4]]
    if prev != nPath[0]: continue

    # 교차로의 신호를 탐색
    for i in nPath[1]:
        nx, ny = x + dirs[i][0], y + dirs[i][1]
        if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
        q.append((nx, ny, time + 1, i))
  
print(answer)