"""
tip > t분 동안 모든 입국 심사대에서 심사가 가능한지 비교.
if 가능 then 범위 줄이기
else then 범위 늘리기
"""
def isValid(t, times, n) -> bool: # t, times, n 을 입력받아 t분동안 처리할 수 있는 수와 대기자 수 비교
    dumps = 0
    for time in times:
        dumps += t // time
        
    return n <= dumps

def solution(n, times):
    start, end = 1, 1_000_000_000 * 1_000_000_000
    
    while end > start:
        t = (start + end) // 2
        if isValid(t, times, n):
            end = t
        else:
            start = t + 1
        
    return start