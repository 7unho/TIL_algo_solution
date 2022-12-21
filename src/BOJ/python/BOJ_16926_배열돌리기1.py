# import sys
# input = sys.stdin.readline

# # 입력값 : N(행), M(열), R(회전 수)

# N, M, R = map(int, input().split())

# graph = [list(map(int, input().split())) for _ in range(N)]

K = 7


for i in range(2, 100):
    print((i + 1) // 2)