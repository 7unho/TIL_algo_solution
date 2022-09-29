# 강의실 배정
## 입력값 : 강의의 개수 (n), 각 강의의 시작, 종료 시간
## 필요한 강의실의 최소 개수

import sys, heapq
input = sys.stdin.readline

n = int(input())
result = []

array = [list(map(int, input().split())) for _ in range(n)]
array.sort(key=lambda x : x[0])

for i in range(n):
    if len(result) != 0 and result[0] <= array[i][0]:
        heapq.heappop(result)
    heapq.heappush(result, array[i][1])

print(len(result))