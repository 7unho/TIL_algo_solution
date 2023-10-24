def solution(sticker):
    N = len(sticker)

    if N <= 3:
        return max(sticker)

    dp = [[0, 0] for _ in range(N)]
    dp[0][0] = sticker[0]

    dp[1] = [sticker[0], sticker[1]]

    for i in range(2, N - 1):
        # 첫번째 포함
        dp[i][1] = max(dp[i - 2][1] + sticker[i], dp[i - 1][1])

        # 첫번째 포함x
        dp[i][0] = max(dp[i - 2][0] + sticker[i], dp[i - 1][0])

    return max(dp[N - 3][0], dp[N - 2][0], dp[N - 3][1] + sticker[-1], dp[N - 2][1])