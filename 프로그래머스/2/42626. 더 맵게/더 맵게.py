import heapq

def solution(scoville, K):
    answer = 0
    q = []
    for sv in scoville:
        heapq.heappush(q, (sv, -sv))
        
    while True:
        first = heapq.heappop(q)[0]
        if not q:
            answer = -1 if first < K else answer
            break
        
        second = heapq.heappop(q)[0]
        
        if first >= K and second >= K:
            break
        
        newItem = first + (second * 2)
        heapq.heappush(q, (newItem, -newItem))
        answer += 1
            
    return answer