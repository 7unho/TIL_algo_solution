# 1Cm 파란 막대, 노란막대, 2cm 빨간막대
# N = N - 1 * 2 + N - 2
N = int(input())

dp = [-1] * (N + 1)
dp[1] = 2
dp[2] = 5

for i in range(3, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1] * 2

print(dp[N])