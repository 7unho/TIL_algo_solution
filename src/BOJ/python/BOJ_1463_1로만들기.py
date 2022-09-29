# 3으로 나누어 떨어지면 3으로 나눈다.
# 2로 나누어 떨어지면 2로 나눈다
# 1을 뺀다.
N = int(input())
INF = int(1e9)
dp = [INF] * (10 ** 6 + 1)

dp[1] = 0
dp[2] = 1

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + 1
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

print(dp[N])