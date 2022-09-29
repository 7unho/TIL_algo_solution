# 쉬운 계단 수
## 입력값 : 길이 (N), 출력값 : 길이가 N인 계단 수의 개수 % 1000000000

import sys
input = sys.stdin.readline

n = int(input())

d = [[0] * 10 for _ in range(n + 1)]

for i in range(1, 10):
    d[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            d[i][j] = d[i - 1][1]
        elif j == 9:
            d[i][j] = d[i - 1][8]
        else:
            d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]

print(sum(d[n]) % 1000000000)
