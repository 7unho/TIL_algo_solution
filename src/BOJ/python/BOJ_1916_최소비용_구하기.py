# 입력값 : 도시 개수 ( N ), 버스의 수 ( M )
# 출력값 : start -> end 까지의 최소비용
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
dp = [INF] * ( N + 1 )

for _ in range(M):
    start, end, dist = map(int, input().split())

    # 현재 좌표(start) -> 다음 좌표(end)까지 걸리는 거리(dist)
    graph[start].append((end, dist))

def solution(start):
    queue = list()
    heapq.heappush(queue, (start, 0))
    dp[start] = 0

    while queue:
        current, dist = heapq.heappop(queue)

        if dp[current] < dist:
            continue

        for next in graph[current]:
            cost = dist + next[1]

            if cost < dp[next[0]]:
                dp[next[0]] = cost
                heapq.heappush(queue, (next[0], cost))

    

start, end = map(int, input().split())
solution(start)
print(dp[end])