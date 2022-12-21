import sys
from itertools import combinations
input = sys.stdin.readline

# 입력값 : L(큰 길의 둘레 길이), P(우체국의 개수), V(마을의 개수)
# 출력값 : 각 마을과 가장 가까운 우체국 사이 거리들 합의 최솟값(S)
#        해당 경우의 마을의 좌표

V, P, L = map(int, input().split())
towns = list(map(int, input().split()))
INF = float("inf")
answer = INF
answers = list()

for case in list(combinations(towns, P)):
    S = 0
    for town in towns:
        temp = INF
        for x in case:
            temp = min(temp, abs(x - town), L - abs(x - town))
        
        S += temp

    if answer > S:
        answer = S
        answers = list(case)

print(answer)
print(*answers)