# 타일 채우기 (3 * n)의 벽을 2 * 1, 1 * 2의 타일로 채우는 경우의 수

import sys
input = sys.stdin.readline

n = int(input())

answer = 0
if (n * 3) % 2 != 0:
    answer = 0
else:
    d = [0 for _ in range(31)]
    d[2] = 3
    d[4] = 8

    for i in range(6, n + 1):
        d[i] = d[i - 2] * 3 + d[i - 4] * 2

    answer = d[n]

print(answer)
