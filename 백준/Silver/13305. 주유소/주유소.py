import sys
input = sys.stdin.readline

N = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))
answer = dists[0] * costs[0]

cost = costs[0]
for i in range(1, N - 1):
    cost = min(cost, costs[i])
    answer += dists[i] * cost

print(answer)