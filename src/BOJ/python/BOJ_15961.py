# 회전 초밥
## 입력값 : N ( 접시의 수 ), d (초밥의 가짓수), k(연속해서 먹는 접시의 수), c(쿠폰 번호)
## 출력값 : 초밥의 가짓수의 최댓값

import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
array = [int(input()) for _ in range(N)]
array += array[:(k - 1)]

# array k개 단위로 끊어주면서 부분 집합 찾기,
# 찾은 부분 집합 가운데 쿠폰 번호를 포함한 집합에서 중복을 제거한 최댓값 출력
current = []

for i in range(k):
    current.append(array[i])

answer = len(set(current + [c]))
for i in range(k, N + k - 1): #    i:i + k
    del current[0]
    current.append(array[i])

    answer = max(answer, len(set(current + [c])))

print(answer)
