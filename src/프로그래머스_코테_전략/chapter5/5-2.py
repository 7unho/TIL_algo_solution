# 문제 : 0이상의 두 정수 n,m이 주어질 때, n^m을 구해봐

n = 2
m = 10

def solution(m):
    # 종료조건
    if m == 0: return 1 
    if n == 1: return 1
    if n == 0: return 1
    return n * solution(m - 1)

print(solution(m))