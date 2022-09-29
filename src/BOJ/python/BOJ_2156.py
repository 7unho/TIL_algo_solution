# 포도주 시식
## 입력값 : 포도주 잔의 개수 (N) 출력값: 내용물의 최댓값
## 연속된 잔은 두개 까지만

import sys
input = sys.stdin.readline

n = int(input())
array = [0 for _ in range(10001)]

for i in range(n):
    array[i] = int(input())

d = [0 for _ in range(10001)]

d[0] = array[0]
d[1] = d[0] + array[1]
d[2] = max(d[1], d[0] + array[2], array[1] + array[2])

for i in range(3, n):
    d[i] = max(array[i] + d[i - 2], array[i] + array[i - 1] + d[i - 3], d[i - 1])

print(d[n - 1])