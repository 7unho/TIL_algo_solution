"""
dp[거스름돈]

answer = dp[n] % 1_000_000_007
"""
def solution(n, money):
    answer = []
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    
    for m in money:
        for i in range(1, n + 1):
            if m > i: continue
            dp[i] += dp[i - m]
        
    
    return dp[n] % 1000000007