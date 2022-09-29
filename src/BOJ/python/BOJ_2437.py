# 저울
## 입력값 : 측정하려는 값 , 출력값 : 정해진 저울들의 조합으로 할 수 없는 최솟값

import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
weights.sort()
answer = 1

for i in weights:
    if answer < i:
        break
    answer += i

print(answer)
