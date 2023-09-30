import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]: increase[i] = max(increase[i], increase[j] + 1)
        if arr[N - i - 1] > arr[N - j - 1]: decrease[N - 1 - i] = max(decrease[N - i - 1], decrease[N - j - 1] + 1)

for i in range(N):
    dp[i] = increase[i] + decrease[i] - 1

print(max(dp))