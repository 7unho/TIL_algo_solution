"""
k:= 초항
range:= [a, -b] -> x = a, x = n - b, y = 0으로 둘러쌓인 면적
n := k가 초항인 우박수열이 1이 될 때 까지의 횟수
"""
def compute(collatz, a, b, n) -> int:
    """
    [a, b] 까지의 정적분 결과 반환
    """
    if a == n + b: return 0
    if a > n + b: return -1
    res = 0
    
    sA, sB = a, a + 1
    
    for d in range(n + b - a):
        dA, dB = sA + d, sB + d
        aY, bY = collatz[dA], collatz[dB]
        
        if aY == bY:
            res += aY
            continue
            
        res += bY - ((bY - aY) / 2) if aY < bY else aY - ((aY - bY) / 2)
        
    return res
def generate_collatz_sequence(k) -> list:
    """
    우박수열 리스트 반환
    """
    collatz = [k]
    x = 1
    while True:
        nK = k / 2 if k % 2 == 0 else (k * 3) + 1
        collatz.append(nK)
        if nK == 1: break
        k = nK
    return collatz

def solution(k, ranges):
    answer = []
    
    collatz = generate_collatz_sequence(k)
    n = len(collatz) - 1
    
    for a, b in ranges:
        answer.append(compute(collatz, a, b, n))
    return answer