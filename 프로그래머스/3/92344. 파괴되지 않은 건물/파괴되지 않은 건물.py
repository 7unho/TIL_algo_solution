def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # 1. skill 만큼 누적합 배열을 누산
    for type, sx, sy, ex, ey, degree in skill:
         weight = degree if type == 2 else -degree
         dp[sx][sy] += weight
         dp[sx][ey + 1] -= weight
         dp[ex + 1][sy] -= weight
         dp[ex + 1][ey + 1] += weight

    for i in range(n + 1):
         for j in range(1, m + 1):
              dp[i][j] += dp[i][j - 1]

    for i in range(1, n + 1):
         for j in range(m + 1):
              dp[i][j] += dp[i - 1][j]

    # 2. dp와 board를 합산
    for i in range(n):
        for j in range(m):
             board[i][j] += dp[i][j]
             if board[i][j] >= 1: answer += 1

    return answer