# 입력값 : 지름길 (N), 도로의 길이 (D)
import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().split())

# 모든 간선을 연결. ( next, dist )
graph = [[(i + 1, 1)] for i in range(D)]
graph.append([])

# 최대값 10000 이상으로 초기화
dp = [10_001] * (D + 1)

for _ in range(1, N + 1):
    start, end, dist = map(int, input().split())

    # end가 target(D) 보다 커진다면 의미가 없으므로 스킵
    if end > D :
        continue

    # start -> (end, dist) : 현재 위치(start)에서 다음 위치(end)까지 가는 거리(dist)
    graph[start].append((end, dist))


def solution(start):
    queue = list()
    heapq.heappush(queue, (start, 0))
    dp[0] = 0

    while queue:
        current, dist = heapq.heappop(queue)

        # current의 최소 거리가 산출된 상태라면
        if dp[current] < dist:
            continue

        # 인접 노드 탐색
        for next in graph[current]:

            # cost = 현재 dist + 다음 좌표까지의 거리
            cost = dist + next[1]

            # cost가 dp[다음 좌표] 보다 작다면 cost로 세팅
            if cost < dp[next[0]]:
                dp[next[0]] = cost
                heapq.heappush(queue, (next[0], cost))

solution(0)

print(dp[D])