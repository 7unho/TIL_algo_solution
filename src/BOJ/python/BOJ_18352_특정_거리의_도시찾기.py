import heapq
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

graph = [list() for _ in range(N + 1)]
distance = [300_001] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append((end, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        # 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
        current, dist = heapq.heappop(q)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[current] < dist:
            continue

        # 현재 노드와 인접한 노드들을 확인
        for next in graph[current]:
            cost = dist + next[1]

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (next[0], cost))

dijkstra(X)
answers = list()

for i in range(1, N + 1):
    if distance[i] == K:
        answers.append(i)
    
if len(answers) == 0:
    print(-1)
else :
    for answer in answers:
        print(answer)