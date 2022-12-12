# 입력값 : V(트리의 정점, 2 ~ 100_000), 정점과 간선의 정보. 입력 마지막은 -1, 거리값은 양수
# 출력값 : 트리의 지름( 임의의 두 점 사이의 거리 중 가장 긴 것 )
import sys
from collections import deque
input = sys.stdin.readline

answer = -1
V = int(input())
points = []

graph = [[] for _ in range(V + 1)]

# 인접 리스트 구현
for _ in range(V):
    li = list(map(int, input().split()))

    for i in range(1, len(li) - 1, 2):
        graph[li[0]].append((li[i], li[i + 1]))

def bfs(x):
    q = deque([x])
    visited = [-1] * (V + 1)
    visited[x] = 0

    answer = (0, 0) # 거리와 노드
    
    while q:
        nx = q.popleft()
        for node, dist in graph[nx]:
            if visited[node] == -1:
                visited[node] = visited[nx] + dist
                q.append(node)

                if answer[0] < visited[node]:
                    answer = (visited[node], node)

    return answer

dist, node = bfs(1)
dist, node = bfs(node)

print(dist)