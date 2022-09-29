## 1, 4, 6원의 화폐 단위 고정
import sys
input = sys.stdin.readline

N = int(input())
dp = [-1] * (N + 1)
dp[0] = 0

for i in range(1, N + 1):
    minimum = int(1e9)

    minimum = min(minimum, dp[i - 1] + 1)
    if i >= 4 : minimum = min(minimum, dp[i - 4] + 1)
    if i >= 6 : minimum = min(minimum, dp[i - 6] + 1)

    dp[i] = minimum

print(dp[N])
print(dp)