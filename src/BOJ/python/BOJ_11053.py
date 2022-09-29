# 가장 긴 증가하는 부분 수열

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))