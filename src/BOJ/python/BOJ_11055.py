# 가장 큰 증가하는 부분 수열
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [item for item in array]
for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])
print(max(dp))
