# 입력값 : 수빈이의 위치 N, 동생의 위치 K
# 출력값 : 수빈이가 동생을 찾는 가장 빠른 시간과 가장 빠른 시간으로 동생을 찾는 경우의 수
## (X - 1), (X + 1), (2 * X) 의 이동
### 위치 좌표는 0 ~ 100,000
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dist = [0] * (10 ** 5 + 1)
dist[N] = 0
queue = deque([N])
cnt = 0

while queue:
    v = queue.popleft()

    # 동생 위치를 찾았다면, 경우의 수 + 1
    if v == K:
        cnt += 1

    for nx in [v - 1, v + 1, v * 2]:
        # nx가 범위 안에 있으면서, 방문한 적 없거나, 현재 +1 인 경우
        if 0 <= nx <= 10 ** 5 and (dist[nx] == -1 or dist[nx] == dist[v] + 1):
            dist[nx] = dist[v] + 1
            queue.append(nx)

print(dist[K])
print(cnt)