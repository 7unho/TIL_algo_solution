# 입력값 : n(노드의 개수), 간선의 정보(부모노드, 자식노드, 양의 가중치)
# 출력값 : 트리의 지름

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    parent, child, dist = map(int, input().split())
    graph[parent].append((child, dist))
    graph[child].append((parent, dist))
    


def bfs(start):
    q = deque([start])
    visited = [-1] * (n + 1)
    visited[start] = 0
    
    # 가장 먼 정점 정보( 노드 번호, 가중치 합 )
    MAX = (0, 0)

    while q:
        x = q.popleft()

        for nx, dist in graph[x]:
            if visited[nx] >= 0: continue

            visited[nx] = visited[x] + dist
            q.append(nx)

            if MAX[1] < visited[nx]:
                MAX = (nx, visited[nx])

    return MAX
# 트리의 지름 : 임의의 정점에서 가장 먼 노드를 찾고(point)
point = bfs(1)
# point로부터 가장 먼 정점까지의 거리
answer = bfs(point[0])

print(answer[1])

