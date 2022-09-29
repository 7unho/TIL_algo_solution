# 숨바꼭질
## 입력값 : N (술래의 위치), K (타겟의 위치) 출력값 : 타겟을 찾는 가장 빠른 시간

from collections import deque
import sys
input = sys.stdin.readline
MAX = 10 ** 6

n, k = map(int, input().split())
queue = deque([n])
dist = [0] * (MAX + 1)

while queue:
    v = queue.popleft()
    if v == k:
        print(dist[v])
        break

    for node in [v - 1, v + 1, v * 2]:
        if 0 <= node <= MAX and not dist[node]:
            dist[node] = dist[v] + 1
            queue.append(node)
