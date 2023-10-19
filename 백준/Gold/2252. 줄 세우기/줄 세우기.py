"""
[백준 2252] 줄 세우기
https://www.acmicpc.net/problem/2252

n := 학생의 수
m := 간선 수

answer = 학생 리스트
"""
# 라이브러리 임포트
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
inDegrees = [0 for _ in range(N + 1)] # 진입차수
graph = [[] for _ in range(N + 1)]
answer = []

for _ in range(M):
    a, b = map(int, input().split()) # 3 1 -> 1이 선행되어야 함
    graph[a].append(b)
    inDegrees[b] += 1

q = deque([])

for i in range(1, N + 1):
    if inDegrees[i] == 0: q.append(i)

while q:
    x = q.popleft()
    answer.append(x)

    for nx in graph[x]:
        inDegrees[nx] -= 1
        
        if inDegrees[nx] == 0:
            q.append(nx)

print(*answer)