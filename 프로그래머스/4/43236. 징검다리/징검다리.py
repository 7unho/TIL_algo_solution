"""
distance := 거리
rocks := 바위 위치
n := 제거할 바위의 수

answer := 최소 거리의 최댓값

모든 지점 사이의 거리가 d이상인 거리의 최댓값.
d를 중심으로 이진탐색..
"""
def isValid(d, rocks, n):
    removed = 0
    last = 0
    
    for rock in rocks:
        if rock - last < d:
            removed += 1
            continue
            
        last = rock
    return removed <= n

def solution(distance, rocks, n):
    start, end = 1, distance + 1
    rocks.append(distance)
    rocks.sort()
    
    while (end - start) > 1:
        mid = (start + end) // 2
        
        if isValid(mid, rocks, n):
            start = mid
        else:
            end = mid
        
    return start