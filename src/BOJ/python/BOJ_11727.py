# 2 * N 타일링 2

import sys
input = sys.stdin.readline

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, (n + 1)):
    d[i] = d[i - 1] + d[i - 2] * 2

print(d[n] % 10007)