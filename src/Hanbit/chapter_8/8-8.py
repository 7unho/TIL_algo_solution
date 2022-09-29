# 효율적인 화폐 구성
## N 종류의 화폐가 있을 때, 가치의 합이 M원이 되는 최소한의 갯수
### 입력값 : N(화폐의 종류), 출력값 : 최소 화폐갯수, 불가할 경우 '-1'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]

# M의 범위보다 큰 값으로 초기화
dp = [10001] * (M + 1)

# 0원을 만드는 화폐의 개수는 0개이므로 dp[0] = 0으로 초기화
dp[0] = 0

# 화폐 종류별로 반복문 돌림
for coin in array:
    for i in range(coin, M + 1):
        if dp[i - coin] != 10001:
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[M] if dp[M] != 10001 else -1)