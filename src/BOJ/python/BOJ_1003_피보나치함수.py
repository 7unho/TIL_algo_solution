import sys
input = sys.stdin.readline

# 입력값 : 테케의 수(T), 피보나치 매개변수(N)
# 출력값 : fibo(0) = 0, fibo(1) = 1을 리턴할 때,
#        fibo(n)을 호출했을 때, 출력되는 0과 1의 개수

MAX = 41
dp = [[0, 0] for _ in range(MAX)]

dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, MAX):
    dp[i][0] = dp[i - 2][0] + dp[i - 1][0]
    dp[i][1] = dp[i - 2][1] + dp[i - 1][1]

for _ in range(int(input())):
    N = int(input())
    print(dp[N][0], dp[N][1])