# 2 * 1 타일링
## 입력값 : N, 출력값 : 경우의 수 % 10007

import sys
input = sys.stdin.readline


def solution(x):
    if d[x] != 0:
        return d[x]
    
    d[x] = (solution(x - 1) + solution(x - 2)) % 10007
    return d[x]
    
N = int(input())

d = [0] * (N + 1)
d[1] = 1
d[2] = 2

print(solution(N))