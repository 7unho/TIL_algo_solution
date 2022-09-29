# 가장 긴 감소하는 수열의 최대 길이
import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if array[j] > array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))