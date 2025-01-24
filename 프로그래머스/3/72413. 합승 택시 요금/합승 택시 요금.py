"""
n := 노드 개수
s := 스타트 지점
a := a 집
b := b 집
fares := [node1, node2, cost]
"""
INF = int(1e9)
def solution(n, s, a, b, fares):
    answer = INF
    dp = [[INF if i != j else 0 for j in range(n)] for i in range(n)]
    for n1, n2, cost in fares:
        dp[n1 - 1][n2 - 1] = cost
        dp[n2 - 1][n1 - 1] = cost
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])
    
    for x in range(n):
        answer = min(answer, dp[s - 1][x] + dp[x][a - 1] + dp[x][b - 1])
        
    return answer