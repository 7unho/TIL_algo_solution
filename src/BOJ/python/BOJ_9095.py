# 1, 2, 3 더하기
## 입력값 : N, 출력값 : 1, 2, 3을 조합하여 N을 만드는 경우의 수
import sys
input = sys.stdin.readline

def solution(x):
    if x == 1:
        return 1
    
    if x == 2 :
        return 2
    
    if x == 3:
        return 4
    
    if d[x] != 0:
        return d[x]
    
    d[x] = solution(x - 3) + solution(x - 2) + solution(x - 1)
    return d[x]

T = int(input())
d = [0] * 11

N = [int(input()) for _ in range(T)]

for answer in N:
    print(solution(answer))
    