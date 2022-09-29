# 정수 삼각형
## 입력값 : N , 출력값 : 선택된 노드 합의 최댓값
import sys
input = sys.stdin.readline

N = int(input())

array = [list(map(int, input().split())) for _ in range(N)]

# d 리스트 초기화 할 때, deep copy로 선언하기 !!
d = [[0] * N for _ in range(N)]
d[0][0] = array[0][0]

for i in range(1, N):
    for j in range((i + 1)):
        if j == 0:
            d[i][j] = d[i - 1][j] + array[i][j]
        elif j == i:
            d[i][j] = d[i - 1][j - 1] + array[i][j]
        else:
            d[i][j] = max(d[i - 1][j], d[i - 1][j - 1]) + array[i][j]

print(max(d[N - 1]))