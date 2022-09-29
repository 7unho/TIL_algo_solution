# 동전 1
## N가지의 동전을 조합해 K원을 만드는 경우의 수

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
d = [0 for _ in range(k + 1)]
d[0] = 1

for coin in coins:
    for i in range(1, (k + 1)):
        if i - coin >= 0:
            d[i] = d[i] + d[i - coin]

print(d[k])