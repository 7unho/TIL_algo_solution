# RGB 거리
## 입력값 : N ( 집의 수 ), RGB 리스트 ( 각 집의 색칠 비용 ) 출력값 : 최소비용

import sys
input = sys.stdin.readline

N = int(input())

RGB = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    RGB[i][0] += min(RGB[i - 1][1], RGB[i - 1][2])
    RGB[i][1] += min(RGB[i - 1][0], RGB[i - 1][2])
    RGB[i][2] += min(RGB[i - 1][0], RGB[i - 1][1])

answer = min(RGB[N - 1][0], RGB[N - 1][1], RGB[N - 1][2])
print(answer)
