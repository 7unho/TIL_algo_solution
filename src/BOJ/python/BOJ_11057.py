# 오르막 수
## 입력값 : N 자리수 출력값: 경우의 수 % 10007

import sys
input = sys.stdin.readline

n = int(input())
d = [[0] * 10 for _ in range(n + 1)]
d[1] = [1 for _ in range(10)]

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j, 10):
            d[i][j] += d[i - 1][k]
        

print(sum(d[n]) % 10007)