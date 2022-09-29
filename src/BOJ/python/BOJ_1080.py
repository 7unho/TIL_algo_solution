# 행렬
## N * M의 0과 1로만 이루어진 행렬을 같게 바꾸는 최소 횟수 출력
## 입력값 : N, M, 행렬 정보

def reverse(n, m):
    for i in range(n, n + 3):
        for j in range(m, m + 3):
            a[i][j] = 1 - a[i][j]

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]
answer = 0

for i in range(n - 2):
    for j in range(m - 2):
        if a == b:
            break

        if a[i][j] != b[i][j]:
            reverse(i, j)
            answer += 1


print(answer if a == b else -1)