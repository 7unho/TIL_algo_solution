for tc in range(1, int(input()) + 1):
    N = int(input())

    graph = list(map(int, input().split()))
    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if graph[i] >= graph[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{tc} {max(dp)}")