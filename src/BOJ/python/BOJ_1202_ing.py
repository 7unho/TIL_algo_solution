# 보석 도둑

## 입력값 : N(보석의 개수), K(가방의 개수)
##        각 보석의 정보(무게 : M, 가격 : V)
##        각 가방의 정보(무게 : C)

import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())

jewels = []

for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((-v, m))

heapq.heapify(jewels)
bags = [int(input()) for _ in range(k)]
bags.sort()
answer = 0
jew_temp = []
for i in range(k):
    while jewels and bags[i] >= jewels[0][1]:
        max_heap = heapq.heappop(jewels)
        heapq.heappush(jew_temp, max_heap)
    
    if jew_temp:
        answer -= heapq.heappop(jew_temp)
    elif not jewels:
        break
        
print(answer)