# 카드 정렬하기

import sys, heapq
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    heapq.heappush(array, int(input()))
    
answer = 0
while True:
    if len(array) == 1:
        break

    sum = heapq.heappop(array) + heapq.heappop(array)
    answer += sum
    heapq.heappush(array, sum)

print(answer)
