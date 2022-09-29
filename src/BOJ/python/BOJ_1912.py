# 연속합
## 입력값 : 정수를 가진 리스트의 길이 (N), 출력값 : 연속된 수들의 합의 최대

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

d = [0] * N
d[0] = array[0]

for i in range(1, N):
    d[i] = max(array[i], d[i - 1] + array[i])

print(max(d))