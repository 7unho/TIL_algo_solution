import heapq

def solution(jobs):
    N = len(jobs)
    scheduler = initScheduler(jobs)
    answer, cursor = 0, 0

    while scheduler:
        valid = list()

        while scheduler:
            req, duration = heapq.heappop(scheduler)
            if req > cursor: 
                heapq.heappush(scheduler, (req, duration))
                break
            heapq.heappush(valid, (duration, req))
        
        if not valid: 
            cursor += 1
            continue

        duration, req = heapq.heappop(valid)
        answer += cursor + duration - req
        cursor += duration
    
        while valid:
            duration, req = heapq.heappop(valid)
            heapq.heappush(scheduler, (req, duration))

    return answer // N

def initScheduler(jobs) -> list:
    """소요시간으로 정렬된 스케줄러 반환"""
    scheduler = list()
    
    for req, duration in jobs:
            heapq.heappush(scheduler, (req, duration))
            
    return scheduler