def solution(n):
    n = str(n)
    return [int(n[i]) for i in range(len(n) - 1, -1, -1)]