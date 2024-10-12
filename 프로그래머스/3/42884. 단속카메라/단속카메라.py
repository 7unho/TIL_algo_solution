def solution(routes):
    answer = 0
    last = -30001
    routes.sort(key=lambda x:x[1])
    
    for start, end in routes:
        if isIntersecting(last, start, end):
            continue
        last = end
        answer += 1
    
    return answer

def isIntersecting(last, start, end):
    return True if last >= start and last <= end else False