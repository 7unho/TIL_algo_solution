## 4, 6원의 화폐 단위 고정
## 화폐 개수의 최댓값은 : 가장작은 화폐로만 구성했을 경우. -> INF를 적절히 잡는다
import sys
input = sys.stdin.readline

N = int(input())
dp = [-1] * (N + 1)
dp[0] = 0

INF = 100000 ## 목표금액이 100000일 경우 아무리 조합을 해도 화폐의 개수가 100000을 넘지 않는다.

for i in range(1, N + 1):
    minimum = INF

    if i >= 4 : minimum = min(minimum, dp[i - 4] + 1)
    if i >= 6 : minimum = min(minimum, dp[i - 6] + 1)

    dp[i] = minimum

print(dp[N]if dp[N] != INF else -1)
print(dp)