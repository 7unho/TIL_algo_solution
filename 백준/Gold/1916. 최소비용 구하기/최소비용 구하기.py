import sys, heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [list() for _ in range(N + 1)]
INF = int(1e9)
dp = [INF] * (N + 1)

for _ in range(M):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))

start, target = map(int, input().split())

def solution(start):
    q = list()
    heapq.heappush(q, (0, start))
    dp[start] = 0
    
    while q:
        dist, current = heapq.heappop(q)
        
        if dist > dp[current]:
            continue
        
        for next in graph[current]:
            cost = dist + next[1]
            
            if cost < dp[next[0]]:
                dp[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
                
solution(start)

print(dp[target])