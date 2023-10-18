answer = 0

# def process(depth, idx, triangle, total):
#     global answer
#     if depth >= len(triangle):
#         answer = max(answer, total)
#         return
    
#     for i in range(idx, idx + 2):
#         process(depth + 1, i, triangle, total + triangle[depth][i])
            

def solution(triangle):
    dp = [[0 for _ in range(len(triangle[i]))] for i in range(len(triangle))]
    dp[0][0] = triangle[0][0]
        
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            dp[i][j] = triangle[i][j]
            if j == 0:
                dp[i][j] += dp[i - 1][j]
                continue
            
            if j == len(triangle[i]) - 1:
                dp[i][j] += dp[i - 1][j - 1]
                continue
                
            dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])

    return max(dp[-1])