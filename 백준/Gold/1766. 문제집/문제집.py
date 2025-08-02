"""
위상 정렬

조건: 사이클이 없는 방향 그래프일 경우에만 가능

동작 과정
1. 진입 차수가 0인 노드를 큐에 삽입
   반복
   1. 방문 노드의 진입 차수 관련 간선을 삭제
   2. 다시 진입 차수가 0인 노드를 큐에 삽입


"""
# 라이브러리 임포트
from collections import deque
import sys, heapq
input = sys.stdin.readline

nodes, edges = map(int, input().split())

inDegrees = [0 for _ in range(nodes + 1)]
graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegrees[b] += 1

q = []
answer = []

for node in range(1, nodes + 1):
    if inDegrees[node]: continue
    heapq.heappush(q, node)

while q:
    node = heapq.heappop(q)
    answer.append(node)

    for next in graph[node]:
        inDegrees[next] -= 1
        if not inDegrees[next]: heapq.heappush(q, next)

print(*answer, sep=' ')