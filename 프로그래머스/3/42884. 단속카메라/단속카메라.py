def solution(routes):
    answer = 0
    last = 30001
    routes.sort(key=lambda x:x[0], reverse=True)
    
    for start, end in routes:
        if isIntersecting(last, start, end):
            continue
        last = start
        answer += 1
    
    return answer

def isIntersecting(last, start, end):
    return True if last >= start and last <= end else False