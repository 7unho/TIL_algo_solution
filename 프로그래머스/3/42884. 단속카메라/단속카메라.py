def solution(routes):
    answer = 0
    last = -int(1e9)
    routes.sort(key=lambda x:x[1])
    
    for start, end in routes:
        if isIntersecting(last, start, end):
            continue
        last = end
        answer += 1
    
    return answer

def isIntersecting(last, start, end):
    return True if last >= start and last <= end else False