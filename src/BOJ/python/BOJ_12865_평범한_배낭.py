# 평범한 배낭
## K의 무게를 버티는 배낭에 가치가 V인 물건 N개를 입력
## 가치의 최댓값을 출력
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# d[N개의 물건][K의 무게] -> 즉 d[n][k]가 원하는 값이 된다.
d = [[0] * (k + 1) for _ in range(n + 1)]
array = [list(map(int, input().split())) for _ in range(n)]

# 인덱싱의 편의를 위해 덤프값 인서트
array.insert(0, [0, 0])


for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = array[i][0]
        v = array[i][1]

        #  현재 물건이 현재 들고 가방의 범위보다 크다면, 저장하지 못하므로
        ## d[현재물건][현재무게] = d[이전물건][같은무게]의 값을 저장한다.
        if j < w:
            d[i][j] = d[i - 1][j]

        # 현재 물건이 현재 들고 있는 가방의 범위보다 작거나 같다면,
        ## d[현재물건][현재무게] = d[이전물건][현재무게]와 d[이전물건][이전무게] + 현재물건의 값어치 중 큰 값으로 저장한다.
        ## d[i - 1][j - w] + v -> 이전 단계에 현재 밸류를 더한 값.
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - w] + v)        

print(d[n][k])