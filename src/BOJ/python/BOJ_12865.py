# 평범한 배낭
## K의 무게를 버티는 배낭에 가치가 V인 물건 N개를 입력
## 가치의 최댓값을 출력
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

d = [[0] * (k + 1) for _ in range(n + 1)]
array = [list(map(int, input().split())) for _ in range(n)]
array.insert(0, [0, 0])

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = array[i][0]
        v = array[i][1]

        if j < w:
            d[i][j] = d[i - 1][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - w] + v)        

print(d[n][k])
