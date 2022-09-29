# 카드 구매하기
## 입력값 : N (카드의 개수), 카드팩의 금액 출력값 : 지불액의 최댓값

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [0 for _ in range(n + 1)]

dp[1] = array[0]

for i in range(2, n + 1):
    temp = []
    for j in range(1, (i + 1)):
        temp.append(dp[i - j] + array[j - 1])
    dp[i] = max(temp)

print(dp[n])