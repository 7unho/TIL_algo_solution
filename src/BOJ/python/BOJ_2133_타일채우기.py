# 타일 채우기 (3 * n)의 벽을 2 * 1, 1 * 2의 타일로 채우는 경우의 수

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (30 + 1)
dp[2] = 3
if (N * 3) % 2 != 0:
    print(0)
    exit(0)

for i in range(4, (N + 1), 2):
    dp[i] += dp[i - 2] * dp[2]
    
    for j in range(2, i - 4 + 1):
       dp[i] += dp[j] * 2
    dp[i] += 2

print(dp[N])