# 바닥 공사
## 가로가 N, 세로의 길이가 2인 직사각형의 바닥
## (1 * 2), (2 * 1), (2 * 2)의 덮개로 바닥을 채우고자 할 때, 경우의 수 % 796,796 구하기
### 입력값 : N, 출력값 : 경우의 수

import sys
input = sys.stdin.readline

N = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(2, N + 1):

    d[i] = (d[i - 2] + d[i - 1] * 2) % 796796

print(d[N])
