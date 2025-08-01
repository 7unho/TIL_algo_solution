dp = [[[None for _ in range(101)] for _ in range(101)] for _ in range(101)]

def process(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        dp[a + 50][b + 50][c + 50] = 1
        return 1
    
    if a > 20 or b > 20 or c > 20:
        if dp[a + 50][b + 50][c + 50] != None:
            return dp[a + 50][b + 50][c + 50]
        dp[a + 50][b + 50][c + 50] = process(20, 20, 20)
        return dp[a + 50][b + 50][c + 50]
    
    if a < b < c:
        if dp[a + 50][b + 50][c + 50] != None:
            return dp[a + 50][b + 50][c + 50]
        dp[a + 50][b + 50][c + 50] = process(a, b, c - 1) + process(a, b - 1, c - 1) - process(a, b - 1, c)
        return dp[a + 50][b + 50][c + 50]
    
    if dp[a + 50][b + 50][c + 50] != None:
        return dp[a + 50][b + 50][c + 50]
    dp[a + 50][b + 50][c + 50] = process(a - 1, b, c) + process(a - 1, b - 1, c) + process(a - 1, b, c - 1) - process(a - 1, b - 1, c - 1)
    return dp[a + 50][b + 50][c + 50]

while True:
    a, b, c = list(map(int, input().split(" ")))
    if (a, b, c) == (-1, -1, -1):
        break

    print(f"w({a}, {b}, {c}) = {process(a, b, c)}")