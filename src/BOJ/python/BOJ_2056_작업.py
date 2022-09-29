from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

# 진입 차수 리스트
indegree = [0] * (N + 1)

# 작업 시간 리스트
values = [0] * (N + 1)

# dp[K] -> K번 쨰 수를 제거할 때 최소 작업 시간
dp = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(1, N + 1):

    # i의 작업시간, 진입 차수 개수, 진출 노드
    value, edge_cnt, *edge_list = map(int, input().split())
    values[i] = value
    indegree[i] = edge_cnt
    
    for end in edge_list:
        graph[end].append(i)

q = deque()

temp = 0
for i in range(1, N + 1):

    # 진입 차수가 없다면
    if indegree[i] == 0:
        q.append(i)

        # dp 초기화
        dp[i] = values[i]

while q:
    current = q.popleft()

    # 진출 차수 간선 제거
    for i in graph[current]:
        indegree[i] -= 1

        # dp[i](queue 같은 단계에 있는 다른 노드의 DP값)와 current(진입 노드) + 현재 노드의 작업시간 중 큰 값으로 세팅
        dp[i] = max(dp[i], dp[current] + values[i])

        if indegree[i] == 0:
            q.append(i)

print(max(dp))