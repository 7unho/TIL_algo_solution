from collections import defaultdict
from random import choices
import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())

graph = [int(input()) for _ in range(N)]
graph += graph[:(k - 1)]

choices = [0 for i in range(d + 1)]
choices[c] = 1

start = 0
window = 0
answer = 1
cnt = 1
for end in range(len(graph)):
    window += 1
    
    choices[graph[end]] += 1
    cnt = cnt + 1 if choices[graph[end]] == 1 else cnt

    if window > k:
        window -= 1
        choices[graph[start]] -= 1
        cnt = cnt - 1 if choices[graph[start]] == 0 else cnt
        start += 1
    
    answer = max(answer, cnt)

print(answer)
