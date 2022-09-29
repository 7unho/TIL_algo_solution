# 연속합 2
# 입력값 : 입력할 수의 개수 ( N ), 출력값 : 연속된 수열의 최댓값 ( 원소 하나를 삭제해도 된다 )

import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.insert(0, 0)
dp = [0] * (N + 1)
cnt = 0

# cnt = 0일 땐, 제거 한 값이 큰지, 제거 안하고 더한 값이 큰지 비교
# cnt = 1일 땐, dp[i - 1] 이 큰지, dp[i - 1] + array[i - 1] 이 큰지 비교.
for i in range(1, (N + 1)):
    if cnt == 1:
        dp[i] = max(dp[i - 1], dp[i - 1] + array[i])
